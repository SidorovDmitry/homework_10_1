from typing import Iterable


def filter_by_currency(transactions: list[dict], currency: str) -> Iterable:
    """Функция фильтрации списка словарей по заданной валюте"""

    return (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    )


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(5):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Больше нет данных")
        break


def transaction_descriptions(transactions: list[dict]) -> Iterable:
    """Функция для генератора списков, которая принимает на вход список словарей и возвращает описание каждой
    операции по очереди"""
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Больше нет данных")
        break