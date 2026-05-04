# tests/test_config.py
# Structural tests for SYSTEM_PROMPT_TEMPLATE: placeholder contract.
from src.config import SYSTEM_PROMPT_TEMPLATE


class TestSystemPromptTemplate:
    def test_contains_user_placeholders(self):
        assert "{first_name}" in SYSTEM_PROMPT_TEMPLATE
        assert "{last_name}" in SYSTEM_PROMPT_TEMPLATE
        assert "{email}" in SYSTEM_PROMPT_TEMPLATE

    def test_formats_without_error_with_valid_user_data(self):
        formatted = SYSTEM_PROMPT_TEMPLATE.format(
            first_name="Jean", last_name="Dupont", email="jean@example.com"
        )
        assert isinstance(formatted, str)
        assert len(formatted) > 0
