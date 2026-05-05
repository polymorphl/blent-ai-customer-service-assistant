from unittest.mock import MagicMock
from src.router import make_router


class TestMakeRouter:
    def _router_with(self, llm_response: str):
        mock_chain = MagicMock()
        mock_chain.invoke.return_value = llm_response
        return make_router(chain=mock_chain)

    def test_returns_true_for_in_scope_question(self):
        is_in_scope = self._router_with("oui")
        assert is_in_scope("Où est ma commande ?") is True

    def test_returns_false_for_out_of_scope_question(self):
        is_in_scope = self._router_with("non")
        assert is_in_scope("Quelle est la capitale de la France ?") is False

    def test_returns_true_on_llm_exception(self):
        mock_chain = MagicMock()
        mock_chain.invoke.side_effect = Exception("API error")
        is_in_scope = make_router(chain=mock_chain)
        assert is_in_scope("Quelque chose") is True

    def test_case_insensitive_oui_match(self):
        is_in_scope = self._router_with("Oui, cela concerne bien le service client.")
        assert is_in_scope("Ma commande est en retard.") is True

    def test_returns_false_for_empty_response(self):
        is_in_scope = self._router_with("")
        assert is_in_scope("Quelque chose") is False

    def test_returns_false_for_unrecognised_response(self):
        is_in_scope = self._router_with("Je ne sais pas")
        assert is_in_scope("Quelque chose") is False
