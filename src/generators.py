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
