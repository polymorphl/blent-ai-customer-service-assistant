from dotenv import load_dotenv

from src.agent import create_agent
from src.config import MSG_GOODBYE, MSG_QUIT_HINT, MSG_READY, MSG_USER_NOT_FOUND, PROMPT_ASSISTANT, PROMPT_USER
from src.database import query

load_dotenv()


def _get_user_by_email(email: str) -> dict | None:
    rows = query("SELECT * FROM users WHERE email = ?", (email,))
    return rows[0] if rows else None


def main():
    email = "leo.cras.vehicula@outlook.com"  # user_id=32, used for local testing
    user = _get_user_by_email(email)
    if not user:
        print(MSG_USER_NOT_FOUND.format(email=email))
        return

    agent = create_agent(
        user_id=user["user_id"],
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=user["email"],
    )

    print(MSG_READY.format(first_name=user["first_name"], last_name=user["last_name"]))
    print(MSG_QUIT_HINT)

    while True:
        try:
            question = input(PROMPT_USER).strip()
            if not question:
                continue
            try:
                response = agent.invoke({"messages": [{"role": "user", "content": question}]})
                answer = response["messages"][-1].content
            except Exception as e:
                if hasattr(e, "response") and e.response.status_code == 401:
                    print("\n[Erreur] Clé API Mistral invalide. Vérifiez MISTRAL_API_KEY dans votre fichier .env.\n")
                else:
                    print(f"\n[Erreur] Impossible de contacter l'assistant : {e}\n")
                continue
            print(PROMPT_ASSISTANT.format(answer=answer))
        except (KeyboardInterrupt, EOFError):
            print(MSG_GOODBYE)
            break


if __name__ == "__main__":
    main()
