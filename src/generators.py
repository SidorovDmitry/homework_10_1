from typing import Iterable, Generator


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


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция для генератора номеров банковских карт, который принимает на вход начальное и конечное значение
    карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты и возвращает номера корт"""
    if start > stop:
        raise ValueError("Стартовое значение не может быть больше конечного")

    for i in range(start, stop + 1):
        new_number_card = str(i).zfill(16)
        formatted_card = f"{new_number_card[:4]} {new_number_card[4:8]} {new_number_card[8:12]} {new_number_card[12:]}"
        yield formatted_card


for card in card_number_generator(1, 5):
    print(card)
