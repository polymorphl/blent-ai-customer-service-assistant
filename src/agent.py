import os

from langchain.agents import create_agent as create_react_agent
from langchain_mistralai import ChatMistralAI

from src.config import LLM_MODEL, SYSTEM_PROMPT_TEMPLATE
from src.tools import make_tools


def create_agent(user_id: int, first_name: str, last_name: str, email: str):
    if not os.getenv("MISTRAL_API_KEY"):
        raise EnvironmentError("MISTRAL_API_KEY is not set. Copy .env.example to .env and fill in your API key.")

    llm = ChatMistralAI(model=LLM_MODEL)
    tools = make_tools(user_id=user_id)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    return create_react_agent(llm, tools, system_prompt=system_prompt)
