import pytest


# Тестируемая функция
def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    return [transaction for transaction in transactions if transaction.get("state") == state]


# Параметризованные тесты
@pytest.mark.parametrize(
    "transactions, state, expected",
    [
        # Тест 1: Фильтрация по "EXECUTED"
        (
            [
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "PENDING", "date": "2023-09-15"},
                {"state": "EXECUTED", "date": "2023-10-05"},
            ],
            "EXECUTED",
            [
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "EXECUTED", "date": "2023-10-05"},
            ],
        ),
        # Тест 2: Фильтрация по "PENDING"
        (
            [
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "PENDING", "date": "2023-09-15"},
                {"state": "EXECUTED", "date": "2023-10-05"},
            ],
            "PENDING",
            [
                {"state": "PENDING", "date": "2023-09-15"},
            ],
        ),
        # Тест 3: Пустой список транзакций
        ([], "EXECUTED", []),
        # Тест 4: Нет подходящих транзакций
        (
            [
                {"state": "CANCELED", "date": "2023-10-01"},
                {"state": "PENDING", "date": "2023-09-15"},
            ],
            "EXECUTED",
            [],
        ),
    ],
)
def test_filter_by_state(transactions, state, expected):
    assert filter_by_state(transactions, state) == expected


# Тестируемая функция
def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)


# Параметризованные тесты
@pytest.mark.parametrize(
    "transactions, reverse, expected",
    [
        # Тест 1: Сортировка по убыванию (по умолчанию)
        (
            [
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "EXECUTED", "date": "2023-10-05"},
                {"state": "EXECUTED", "date": "2023-09-15"},
            ],
            True,
            [
                {"state": "EXECUTED", "date": "2023-10-05"},
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "EXECUTED", "date": "2023-09-15"},
            ],
        ),
        # Тест 2: Сортировка по возрастанию
        (
            [
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "EXECUTED", "date": "2023-10-05"},
                {"state": "EXECUTED", "date": "2023-09-15"},
            ],
            False,
            [
                {"state": "EXECUTED", "date": "2023-09-15"},
                {"state": "EXECUTED", "date": "2023-10-01"},
                {"state": "EXECUTED", "date": "2023-10-05"},
            ],
        ),
        # Тест 3: Пустой список транзакций
        ([], True, []),
        # Тест 4: Одна транзакция
        (
            [{"state": "EXECUTED", "date": "2023-10-01"}],
            True,
            [{"state": "EXECUTED", "date": "2023-10-01"}],
        ),
    ],
)
def test_sort_by_date(transactions, reverse, expected):
    assert sort_by_date(transactions, reverse) == expected
