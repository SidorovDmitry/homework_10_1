from typing import Dict, Generator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """Фильтрует транзакции по заданной валюте с обработкой ошибок"""
    if not isinstance(transactions, list):
        return

    currency = str(currency).upper() if currency else ""

    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue

        try:
            # Проверяем стандартный формат с operationAmount
            if "operationAmount" in transaction:
                op_amount = transaction["operationAmount"]
                if isinstance(op_amount, dict):
                    curr = op_amount.get("currency", {})
                    if isinstance(curr, dict):
                        code = str(curr.get("code", "")).upper()
                        if code == currency:
                            yield transaction
                            continue

            # Проверяем альтернативный формат с currency_code
            code = str(transaction.get("currency_code", "")).upper()
            if code == currency:
                yield transaction

        except (AttributeError, TypeError):
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
