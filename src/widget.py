from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: str) -> str:
    """Функция принимает на вход строку с номером карты или счета и возвращает замаскированный номер"""

    # Удаляем лишние пробелы в начале и конце строки
    card_account_number = card_account_number.strip()

    # Проверяем, что строка не пустая
    if not card_account_number:
        raise ValueError("Входная строка пустая")

    parts = card_account_number.split()

    # Проверяем, является ли последний элемент числом (номер карты или счета)
    if not parts[-1].isdigit():
        raise ValueError("Некорректный формат: отсутствует номер карты или счета")

    # Определяем тип (карта или счет)
    if "Счет" in card_account_number:
        if len(parts) != 2 or len(parts[-1]) != 20:
            raise ValueError("Некорректный формат счета")
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        # Обрабатываем карту
        if len(parts) < 2 or len(parts[-1]) != 16:
            raise ValueError("Некорректный формат карты")
        card_number = parts[-1]
        masked_number = get_mask_card_number(card_number)
        card_name = " ".join(parts[:-1])
        return f"{card_name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Функция принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'.
    Если формат входной строки некорректен, возвращает "Некорректный формат даты".
    """
    try:
        if "T" not in date_string:
            return "Некорректный формат даты"

        date_part, time_part = date_string.split("T")
        year, month, day = date_part.split("-")

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Некорректный формат даты"

        # Проверяем, что после времени нет лишних символов
        if len(time_part.split(".")) > 2 or time_part.endswith("Z"):
            return "Некорректный формат даты"

        # Проверяем корректность значений месяца и дня
        if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            return "Некорректный формат даты"

        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    except (IndexError, ValueError):
        return "Некорректный формат даты"
