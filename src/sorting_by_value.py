import re
from collections import Counter
from typing import Dict, List


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Фильтрует транзакции по строке поиска в описании."""
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        return [
            transaction
            for transaction in transactions
            if transaction.get("description") and pattern.search(transaction["description"])
        ]
    except re.error:
        print(f"Некорректное регулярное выражение: '{search_string}'")
        return []


def count_operations_by_category(transactions: List[Dict], categories: List[str]):
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, значения — это количество в каждой категории."""

    # Собираем все описания (description) из операций, которые есть в заданном списке категорий
    description_list = [
        transaction.get("description") for transaction in transactions if transaction.get("description") in categories
    ]

    # Используем Counter для подсчета
    description_counts = Counter(description_list)

    # Преобразуем Counter в обычный словарь и добавляем категории с нулевым количеством
    result = {category: description_counts.get(category, 0) for category in categories}

    return result
