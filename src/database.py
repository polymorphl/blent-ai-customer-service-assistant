import sqlite3

from src.config import DB_PATH


def query(sql: str, params: tuple = ()) -> list[dict]:
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        try:
            rows = [dict(row) for row in conn.execute(sql, params).fetchall()]
        finally:
            conn.close()
        return rows
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {e}") from e
