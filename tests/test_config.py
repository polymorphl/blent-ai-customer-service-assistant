# tests/test_config.py
# Structural tests for SYSTEM_PROMPT_TEMPLATE: placeholder contract.
from src.config import MSG_ESCALATION, MSG_OUT_OF_SCOPE, ROUTER_PROMPT, SYSTEM_PROMPT_TEMPLATE


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


class TestRouterConfig:
    def test_router_prompt_has_question_placeholder(self):
        assert "{question}" in ROUTER_PROMPT

    def test_router_prompt_wraps_question_in_xml_delimiters(self):
        assert "<question>{question}</question>" in ROUTER_PROMPT

    def test_msg_out_of_scope_is_non_empty_string(self):
        assert isinstance(MSG_OUT_OF_SCOPE, str)
        assert len(MSG_OUT_OF_SCOPE) > 0


class TestEscalationConfig:
    def test_msg_escalation_is_non_empty_string(self):
        assert isinstance(MSG_ESCALATION, str)
        assert len(MSG_ESCALATION) > 0

    def test_system_prompt_references_escalate_to_human_tool(self):
        assert "escalate_to_human" in SYSTEM_PROMPT_TEMPLATE

    def test_system_prompt_instructs_verbatim_relay(self):
        assert "mot pour mot" in SYSTEM_PROMPT_TEMPLATE
