def get_mask_card_number(number_cards: int | str) -> str:
    """Функция принимает на вход номер карты число и возвращает маску номера"""
    str_cards_number = str(number_cards)  # Преобразуем число в строку

    # Проверяем, что номер карты состоит из 16 цифр
    if len(str_cards_number) != 16 or not str_cards_number.isdigit():
        return "Некорректный номер карты"

    # Формируем маску номера карты
    return f"{str_cards_number[:4]} {str_cards_number[4:6]}** **** {str_cards_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    account_number_str = str(account_number)  # Преобразуем номер счёта в строку

    # Проверяем, что номер счёта состоит только из цифр и имеет достаточную длину
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        return "Некорректный номер счёта"

    # Формируем маску номера счёта
    return "**" + account_number_str[-4:]
