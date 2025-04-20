import pytest
from src.sorting_by_value import filter_transactions
from typing import List, Dict


@pytest.fixture
def sample_transactions() -> List[Dict]:
    return [
        {"id": 1, "description": "Перевод организации", "other_field": "value1"},
        {"id": 2, "description": "Открытие вклада", "other_field": "value2"},
        {"id": 3, "description": "Перевод физическому лицу", "other_field": "value3"},
        {"id": 4, "description": "Покупка товаров", "other_field": "value4"},
        {"id": 5, "description": None, "other_field": "value5"},  # None description
        {"id": 6, "other_field": "value6"},  # Отсутствует description
        {"id": 7, "description": "", "other_field": "value7"},  # Пустая строка
        {"id": 8, "description": "  ", "other_field": "value8"},  # Пробелы
    ]

def test_filter_exact_match(sample_transactions):
    """Тест на точное совпадение"""
    result = filter_transactions(sample_transactions, "Перевод организации")
    assert len(result) == 1
    assert result[0]["id"] == 1

def test_filter_handles_none_description(sample_transactions):
    """Тест обработки None в описании"""
    result = filter_transactions(sample_transactions, "Перевод")
    assert len(result) == 2
    assert {t["id"] for t in result} == {1, 3}

def test_filter_handles_missing_description(sample_transactions):
    """Тест обработки отсутствия поля description"""
    result = filter_transactions(sample_transactions, "value")
    assert len(result) == 0

def test_filter_handles_empty_string(sample_transactions):
    """Тест обработки пустой строки в описании"""
    result = filter_transactions(sample_transactions, "Покупка")
    assert len(result) == 1
    assert result[0]["id"] == 4

def test_filter_with_whitespace(sample_transactions):
    """Тест обработки строки с пробелами"""
    result = filter_transactions(sample_transactions, "  ")
    assert len(result) == 1