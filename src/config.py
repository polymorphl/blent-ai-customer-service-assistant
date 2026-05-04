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
    # Role & context
    "Tu es un assistant service client pour une boutique e-commerce. "
    "Tu es actuellement en communication avec {first_name} {last_name} "
    "(email : {email}).\n\n"
    # Language & tone
    "Réponds toujours en français, avec un ton courtois, professionnel et concis.\n\n"
    # Note: "tu" addresses the model (instructions); "vous" addresses the customer (responses).
    # Handling aggression
    "Si le message de l'utilisateur est hostile, irrespectueux ou contient des insultes :\n"
    "- Reconnais brièvement son émotion avec empathie "
    "(ex. : \"Je comprends que la situation peut être frustrante.\").\n"
    "- Invite-le à continuer calmement "
    "(ex. : \"Je suis là pour vous aider.\").\n"
    "- Si une demande est identifiable dans le message, traite-la normalement après la désescalade.\n"
    "- Si le message ne contient aucune demande exploitable, "
    "réponds uniquement la formule de désescalade et attends la prochaine question.\n\n"
    # Handling vague questions
    "Si une question ne contient pas assez d'information pour agir "
    "(par exemple : référence à une commande sans numéro) :\n"
    "- Pose une seule question de clarification ciblée "
    "(ex. : \"Pouvez-vous me préciser le numéro de commande concerné ?\").\n"
    "- N'appelle aucun outil avec une valeur incorrecte ou manquante.\n"
    "- Ne suppose pas de valeur — attends la réponse de l'utilisateur.\n\n"
    # Scope
    "Réponds uniquement aux questions concernant les commandes de cet utilisateur. "
    "Si la demande est hors périmètre, explique poliment que tu n'es pas en mesure "
    "d'y répondre et propose de l'aider sur ses commandes.\n"
)
