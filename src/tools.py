from datetime import datetime

from langchain_core.tools import tool

from src.config import MONTHS_FR, STATUS_MAPPING
from src.database import query


def make_tools(user_id: int) -> list:
    @tool
    def get_my_orders() -> list[dict]:
        """Returns all orders for the authenticated user."""
        rows = query(
            "SELECT * FROM orders WHERE user_id = ?",
            (user_id,),
        )
        return [_format_order(row) for row in rows]

    @tool
    def get_order_details(order_id: int) -> dict:
        """Returns details for a specific order. Only works for orders belonging to the authenticated user."""
        rows = query(
            "SELECT * FROM orders WHERE order_id = ? AND user_id = ?",
            (order_id, user_id),
        )
        if not rows:
            return {"error": "Commande introuvable"}
        return _format_order(rows[0])

    @tool
    def get_my_delivery_address() -> dict:
        """Returns the delivery address registered on the authenticated user's account."""
        rows = query(
            "SELECT address, city, zip_code FROM users WHERE user_id = ?",
            (user_id,),
        )
        if not rows:
            return {"error": "Utilisateur introuvable"}
        return _format_address(rows[0])

    return [get_my_orders, get_order_details, get_my_delivery_address]


def _format_order(row: dict) -> dict:
    return {
        "order_id": row["order_id"],
        "user_id": row["user_id"],
        "status": STATUS_MAPPING.get(row["status"], row["status"]),
        "date_purchase": _format_date(row["date_purchase"]),
        "date_shipped": _format_date(row["date_shipped"]),
        "date_delivered": _format_date(row["date_delivered"]),
    }


def _format_address(row: dict) -> dict:
    return {
        "address": row["address"],
        "city": row["city"],
        "zip_code": row["zip_code"],
        "formatted": f"{row['address']}, {row['zip_code']} {row['city']}",
    }


def _format_date(date_str: str | None) -> str | None:
    if not date_str:
        return None
    try:
        dt = datetime.fromisoformat(date_str)
        month_name = MONTHS_FR.get(dt.month, str(dt.month))
        return f"{dt.day} {month_name} {dt.year} à {dt.hour:02d}h{dt.minute:02d}"
    except ValueError:
        return date_str
