from typing import Callable

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI

from src.config import LLM_MODEL, ROUTER_PROMPT


def make_router(chain=None) -> Callable[[str], bool]:
    if chain is None:
        llm = ChatMistralAI(model=LLM_MODEL)
        chain = PromptTemplate.from_template(ROUTER_PROMPT) | llm | StrOutputParser()

    def is_in_scope(question: str) -> bool:
        try:
            result = chain.invoke({"question": question})
            return result.strip().lower().startswith("oui")
        except Exception:
            return True  # fail open — agent retains its own guardrails

    return is_in_scope
