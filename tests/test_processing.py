import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура с тестовыми данными функции filter_by_state
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "PENDING"},
        {"id": 4, "state": "executed"},  # Проверка регистра
        {"id": 5, "state": "canceled"},
        {"id": 6, "state": 1},  # Числовой статус (1 = EXECUTED)
        {"id": 7, "state": 2.0},  # Числовой статус (2.0 = CANCELED)
        {"id": 8},  # Нет статуса
        {"id": 9, "state": None},  # None статус
        {"id": 10, "state": "INVALID"},  # Неверный статус
        "invalid_transaction",  # Некорректная транзакция
    ]


# Тесты для успешных сценариев
@pytest.mark.parametrize(
    "state,expected_count",
    [
        ("EXECUTED", 2),
        ("executed", 2),
        ("CANCELED", 2),
        ("PENDING", 1),
        ("pending", 1),
    ],
)
def test_filter_by_state_success(sample_transactions, state, expected_count):
    """Тестирование успешной фильтрации"""
    result = filter_by_state(sample_transactions, state)
    assert len(result) == expected_count
    assert all(str(t["state"]).upper() == state.upper() for t in result)


# Тесты для числовых статусов
def test_numeric_states(sample_transactions):
    """Тестирование числовых статусов"""
    # Предполагаем, что 1 соответствует EXECUTED, 2 - CANCELED и т.д.
    result = filter_by_state(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert {t["id"] for t in result} == {1, 4}


# Тесты для ошибок входных данных
def test_empty_transactions():
    """Тестирование пустого списка транзакций"""
    with pytest.raises(ValueError) as excinfo:
        filter_by_state([], "EXECUTED")
    assert "пустой список транзакций" in str(excinfo.value)


def test_invalid_state():
    """Тестирование недопустимого статуса"""
    with pytest.raises(ValueError) as excinfo:
        filter_by_state([{"state": "EXECUTED"}], "INVALID")
    assert "Недопустимый статус" in str(excinfo.value)
    assert "EXECUTED, CANCELED, PENDING" in str(excinfo.value)


# Тесты для некорректных данных
def test_non_dict_transactions():
    """Тестирование списка с некорректными транзакциями"""
    transactions = ["not_a_dict", 123, None, {"state": "EXECUTED"}]
    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"


def test_none_state():
    """Тестирование транзакций с None статусом"""
    transactions = [{"state": None}, {"state": "EXECUTED"}]
    result = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 1
    assert result[0]["state"] == "EXECUTED"


# Тест для проверки сохранения порядка
def test_order_preservation():
    """Тестирование сохранения порядка транзакций"""
    transactions = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    result = filter_by_state(transactions, "EXECUTED")
    assert [t["id"] for t in result] == [1, 3]


# Параметризованный тест для sort_by_date
def test_sort_by_date(sort_by_date_data):
    for transactions, reverse, expected in sort_by_date_data:
        result = sort_by_date(transactions, reverse)
        assert result == expected
