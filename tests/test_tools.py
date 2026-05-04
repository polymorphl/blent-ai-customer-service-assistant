from src.tools import make_tools


# Seed data facts used in these tests:
# - user_id=32 owns order_id=1 (status=shipped, date_purchase="2024-05-25 22:27:26", date_shipped="2024-05-26 22:27:26", date_delivered=None)
# - user_id=32 owns order_id=48 (status=shipped)
# - user_id=24 owns order_id=2 (status=delivered)
# - user_id=9  owns order_id=8 (status=invoiced)


def _tool(tools, name):
    return next(t for t in tools if t.name == name)


class TestGetMyOrders:
    def test_returns_only_authenticated_user_orders(self):
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_my_orders").invoke({})
        assert all(o["user_id"] == 32 for o in result)

    def test_returns_list_with_expected_orders(self):
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_my_orders").invoke({})
        order_ids = [o["order_id"] for o in result]
        assert 1 in order_ids
        assert 48 in order_ids

    def test_returns_empty_list_for_user_without_orders(self):
        tools = make_tools(user_id=9999)
        result = _tool(tools, "get_my_orders").invoke({})
        assert result == []

    def test_status_mapping_applied(self):
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_my_orders").invoke({})
        statuses = [o["status"] for o in result]
        assert "shipped" not in statuses
        assert "Expédiée — en cours de livraison" in statuses

    def test_invoiced_status_mapping(self):
        tools = make_tools(user_id=9)
        result = _tool(tools, "get_my_orders").invoke({})
        order_8 = next(o for o in result if o["order_id"] == 8)
        assert order_8["status"] == "Validée — en attente d'expédition"


class TestGetOrderDetails:
    def test_returns_order_for_correct_user(self):
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_order_details").invoke({"order_id": 1})
        assert result["order_id"] == 1
        assert result["user_id"] == 32

    def test_rejects_order_belonging_to_other_user(self):
        # order_id=2 belongs to user_id=24, not user_id=32
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_order_details").invoke({"order_id": 2})
        assert "error" in result

    def test_rejects_nonexistent_order(self):
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_order_details").invoke({"order_id": 9999})
        assert "error" in result

    def test_status_mapping_applied(self):
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_order_details").invoke({"order_id": 1})
        assert result["status"] == "Expédiée — en cours de livraison"

    def test_dates_formatted(self):
        # order_id=1: date_purchase="2024-05-25 22:27:26"
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_order_details").invoke({"order_id": 1})
        assert result["date_purchase"] == "25 mai 2024 à 22h27"
        assert result["date_shipped"] == "26 mai 2024 à 22h27"

    def test_null_date_delivered_for_shipped_order(self):
        # order_id=1 is shipped, date_delivered is NULL
        tools = make_tools(user_id=32)
        result = _tool(tools, "get_order_details").invoke({"order_id": 1})
        assert result["date_delivered"] is None
