def get_mask_card_number(number_cards: int) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера"""

    str_cards_number = str(number_cards)  # Преобразуем число в строку
    card_number_length = len(str_cards_number)  # Узнаем длину строки

    if card_number_length != 16:  # Проверяем, что номер карты состоит из 16 цифр
        return "Некорректный номер карты"

    return f"{str_cards_number[:4]} {str_cards_number[4:6]}** **** {str_cards_number[:-4]}"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""

    account_number_str = str(account_number)  # Преобразуем номер счёта в строку

    return "**" + account_number_str[-4:]  # Формируем маску номера счёта





