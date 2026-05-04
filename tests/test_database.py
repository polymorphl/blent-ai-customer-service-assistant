import pytest

from src.database import query


def test_query_raises_runtime_error_on_bad_sql():
    with pytest.raises(RuntimeError, match="Database error"):
        query("SELECT * FROM this_table_does_not_exist", ())


def test_query_returns_list_of_dicts():
    result = query("SELECT * FROM users WHERE user_id = ?", (32,))
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], dict)
    assert result[0]["user_id"] == 32


def test_query_returns_empty_list_when_no_results():
    result = query("SELECT * FROM users WHERE user_id = ?", (9999,))
    assert result == []


def test_query_returns_multiple_rows():
    result = query("SELECT * FROM orders WHERE user_id = ?", (32,))
    assert len(result) >= 2
