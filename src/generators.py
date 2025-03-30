
from typing import Generator, Dict, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """Фильтрует транзакции по заданной валюте"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """Генерирует описания транзакций"""
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генерирует номера карт в заданном диапазоне"""
    for num in range(start, end + 1):
        yield f"{num:016d}"


