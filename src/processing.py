from typing import Any

def filter_by_state(list_dict: list[Any], state: str = "EXECUTED") -> list[Any]:
    """Функция фильтрует данные по указанному параметру 'state'"""

    if not list_dict:
        raise ValueError("Элемент списка не является словарем")
    new_list = []

    for item in list_dict:
        if item.get("state") == state:
            new_list.append(item)
        elif item.get("state") == "":
            raise ValueError("Нет текста")
    return new_list



def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращать новый список, отсортированный по дате"""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)
