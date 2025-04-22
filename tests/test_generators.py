import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transaction,currency,should_match",
    [
        ({"operationAmount": {"currency": {"code": "USD"}}}, "USD", True),
        ({"currency_code": "EUR"}, "EUR", True),
        ({"description": "No currency"}, "USD", False),
        ({"operationAmount": {"currency": {"code": "rub"}}}, "RUB", True),
        ({}, "USD", False),
        (None, "USD", False),
        ({"operationAmount": {"currency": {}}}, "USD", False),
        ({"operationAmount": None}, "USD", False),
        ("invalid_transaction", "USD", False),
        (12345, "USD", False),
        ({"operationAmount": {"currency": {"code": "USD"}}}, "usd", True),
        ({"currency_code": "eur"}, "EUR", True),
    ],
)
def test_filter_by_currency_edge_cases(transaction, currency, should_match):
    """Тестирование граничных случаев"""
    result = list(filter_by_currency([transaction], currency))
    assert (len(result) == 1) == should_match


def test_filter_with_none_transactions():
    """Тестирование с None вместо списка транзакций"""
    assert len(list(filter_by_currency(None, "USD"))) == 0


def test_filter_with_empty_list():
    """Тестирование с пустым списком транзакций"""
    assert len(list(filter_by_currency([], "USD"))) == 0


def test_filter_with_invalid_transactions():
    """Тестирование с некорректными типами транзакций"""
    transactions = [None, "invalid", 123, {}]
    assert len(list(filter_by_currency(transactions, "USD"))) == 0


def test_filter_with_mixed_transactions(sample_transactions):
    """Тестирование со смешанным набором транзакций"""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 3
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"


# Тесты для функции transaction_descriptions
def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions) == 5
    assert all(isinstance(d, str) for d in descriptions)


@pytest.mark.parametrize(
    "transactions,expected_descriptions",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 939719571,
                    "state": "EXECUTED",
                    "date": "2018-07-01T10:15:23.123456",
                    "operationAmount": {
                        "amount": "5000.00",
                        "currency": {"name": "EUR", "code": "EUR"},
                    },
                    "description": "Покупка в магазине",
                    "from": "Счет 12345678901234567890",
                    "to": "Счет 09876543210987654321",
                },
            ],
            ["Перевод организации", "Покупка в магазине"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(transactions, expected_descriptions):
    generated_descriptions = list(transaction_descriptions(transactions))
    assert generated_descriptions == expected_descriptions


def test_card_number_generator():
    numbers = list(card_number_generator(1, 5))
    assert numbers == [
        "0000000000000001",
        "0000000000000002",
        "0000000000000003",
        "0000000000000004",
        "0000000000000005",
    ]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1234567890123456, "1234567890123456"),
        (1234567890123457, "1234567890123457"),
        (1234567890123460, "1234567890123460"),
    ],
)
def test_card_number_generator(test_input, expected):
    assert next(card_number_generator(test_input, test_input)) == expected


def test_card_numbers_length(card_numbers):
    assert len(card_numbers) == 5


def test_card_numbers_format(card_numbers):
    for number in card_numbers:
        assert len(number) == 16
