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
    """функция преобразует дату в формат 'ДД.ММ.ГГГГ'"""

    # Проверка на пустую строку
    if not date_string:
        raise ValueError("Дата не может быть пустой строкой.")

    # Проверка на корректный формат даты
    if "T" not in date_string:
        raise ValueError("Некорректный формат даты. Ожидается 'ГГГГ-ММ-ДДTЧЧ:ММ:СС'.")

    # Разделение строки на 2 части по "Т", а также по "-" части строки с индексом 0
    split_date_string = date_string.split("T")[0].split("-")

    # Проверка на корректное количество частей
    if len(split_date_string) != 3:
        raise ValueError("Некорректный формат даты. Ожидается 'ГГГГ-ММ-ДД'.")

    # Извлечение год, месяц, день
    year, month, day = split_date_string

    # Форматирование даты в нужный формат
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
