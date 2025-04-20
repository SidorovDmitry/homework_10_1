import re
from typing import List, Dict


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """ Фильтрует транзакции по строке поиска в описании."""
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        return [
            transaction
            for transaction in transactions
            if transaction.get('description') and pattern.search(transaction['description'])
        ]
    except re.error:
        print(f"Некорректное регулярное выражение: '{search_string}'")
        return []


