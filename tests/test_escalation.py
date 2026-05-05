import pytest
from src.config import MSG_ESCALATION
from src.tools import make_tools


@pytest.fixture
def escalate():
    tools = make_tools(user_id=1)
    return next(t for t in tools if t.name == "escalate_to_human")


class TestEscalateToHuman:
    def test_returns_escalated_true(self, escalate):
        result = escalate.invoke({"reason": "Demande de remboursement"})
        assert result["escalated"] is True

    def test_returns_msg_escalation_verbatim(self, escalate):
        result = escalate.invoke({"reason": "Litige"})
        assert result["message"] == MSG_ESCALATION

    def test_passes_reason_through(self, escalate):
        result = escalate.invoke({"reason": "Article défectueux reçu"})
        assert result["reason"] == "Article défectueux reçu"

    def test_empty_reason_returns_error(self, escalate):
        result = escalate.invoke({"reason": ""})
        assert "error" in result
        assert result.get("escalated") is not True
