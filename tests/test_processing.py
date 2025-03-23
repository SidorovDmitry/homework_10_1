import pytest
from src.processing import filter_by_state, sort_by_date

# Параметризованный тест для filter_by_state
def test_filter_by_state(filter_by_state_data):
    for transactions, state, expected in filter_by_state_data:
        result = filter_by_state(transactions, state)
        assert result == expected

# Параметризованный тест для sort_by_date
def test_sort_by_date(sort_by_date_data):
    for transactions, reverse, expected in sort_by_date_data:
        result = sort_by_date(transactions, reverse)
        assert result == expected


