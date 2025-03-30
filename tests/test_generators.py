from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

import pytest


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        # Обычный случай: 1 транзакция в USD
        (
            [{"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
        # Нет совпадений
        (
            [{"operationAmount": {"currency": {"code": "EUR"}}}],
            "USD",
            [],
        ),
        # Пропуск транзакции с ошибкой в структуре
        (
            [{"invalid": "data"}, {"operationAmount": {"currency": {"code": "USD"}}}],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions, currency, expected):
    assert list(filter_by_currency(transactions, currency)) == expected


def test_filter_by_currency(sample_transactions):
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 3
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_transactions)


def test_filter_by_currency_with_exceptions():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}},
        {"operationAmount": {"currency": {}}},  # Отсутствие ключа 'code'
        {"operationAmount": {}},  # Отсутствие вложенного словаря 'currency'
        {},  # Пустой словарь
    ]
    currency = "USD"
    filtered_transactions = list(filter_by_currency(transactions, currency))
    assert len(filtered_transactions) == 1, "Ожидается одна транзакция с правильной валютой"
    assert (
        filtered_transactions[0]["operationAmount"]["currency"]["code"] == currency
    ), "Валюта транзакции не соответствует заданной"


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
