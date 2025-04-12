import logging
import os

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "../logs", "masks.log"), mode="w", encoding="utf-8"
)


file_formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")


def get_mask_card_number(number_cards: int | str) -> str:
    """Функция принимает на вход номер карты число и возвращает маску номера"""
    logger.info(get_mask_card_number.__doc__)
    str_cards_number = str(number_cards)  # Преобразуем число в строку

    # Проверяем, что номер карты состоит из 16 цифр
    if len(str_cards_number) != 16 or not str_cards_number.isdigit():
        logger.error("Некорректный номер карты")
        return "Некорректный номер карты"

    # Формируем маску номера карты
    return f"{str_cards_number[:4]} {str_cards_number[4:6]}** **** {str_cards_number[-4:]}"
    logger.info("OK")


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера."""
    logger.info(get_mask_card_number.__doc__)
    account_number_str = str(account_number)  # Преобразуем номер счёта в строку

    # Проверяем, что номер счёта состоит только из цифр и имеет достаточную длину
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        logger.error("Некорректный номер счёта")
        return "Некорректный номер счёта"

    # Формируем маску номера счёта
    return "**" + account_number_str[-4:]
    logger.info("OK")
