from pathlib import Path

# Path to the SQLite database file
DB_PATH = Path(__file__).parent.parent / "seed" / "orders.db"

# Mistral model used by the LangChain agent
LLM_MODEL = "ministral-8b-latest"

# Maps raw database status values to human-readable French labels
STATUS_MAPPING = {
    "invoiced": "Validée — en attente d'expédition",
    "shipped": "Expédiée — en cours de livraison",
    "delivered": "Livrée",
}

# Maps month numbers to French month names, used for date formatting in tool output
MONTHS_FR = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril",
    5: "mai", 6: "juin", 7: "juillet", 8: "août",
    9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre",
}

# CLI messages displayed to the user during a session
MSG_USER_NOT_FOUND = "Utilisateur introuvable : {email}"
MSG_READY = "Assistant prêt — connecté en tant que {first_name} {last_name}."
MSG_QUIT_HINT = "(Ctrl+C pour quitter)\n"
MSG_GOODBYE = "\nAu revoir !"
PROMPT_USER = "Vous : "
PROMPT_ASSISTANT = "\nAssistant : {answer}\n"

# System prompt injected into the agent at session start with the authenticated user's context
SYSTEM_PROMPT_TEMPLATE = (
    "Tu es un assistant service client pour une boutique e-commerce. "
    "Tu es actuellement en communication avec {first_name} {last_name} "
    "(email : {email}). "
    "Réponds uniquement aux questions concernant les commandes de cet utilisateur. "
    "Réponds toujours en français de manière courtoise et concise."
)
