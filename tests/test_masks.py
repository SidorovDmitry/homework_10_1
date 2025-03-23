import pytest
from src.masks import get_mask_account, get_mask_card_number


# Тест, использующий фикстуру как аргумент
def test_get_mask_card_number(card_number_test_data):
    for card_number, expected_result in card_number_test_data:
        result = get_mask_card_number(card_number)
        assert result == expected_result


# Тест, использующий фикстуру как аргумент
def test_get_mask_account(account_number_test_data):
    for account_number, expected_result in account_number_test_data:
        result = get_mask_account(account_number)
        assert result == expected_result
# @pytest.mark.parametrize(
#     "account_number, expected_result",
#     [
#         (73654108430135874305, "**4305"),  # Корректный номер счёта
#         (12345678901234567890, "**7890"),  # Корректный номер счёта
#         (1234, "Некорректный номер счёта"),  # Слишком короткий номер
#         ("fdssdfs", "Некорректный номер счёта"),  # Нечисловые символы
#         ("", "Некорректный номер счёта"),  # Пустая строка
#         ("12345678901234567890", "**7890"),  # Корректный номер счёта (строка)
#     ],
# )
# def test_get_mask_account(account_number: int | str, expected_result: str):
#     assert get_mask_account(account_number) == expected_result
#
# @pytest.mark.parametrize(
#     "card_number, expected_result",
#     [
#         (1234567812345678, "1234 56** **** 5678"),
#         (0, "Некорректный номер карты"),
#         (12345678, "Некорректный номер карты"),
#         (123456781234567812, "Некорректный номер карты"),
#         ("123456781234567A", "Некорректный номер карты"),
#         ("", "Некорректный номер карты"),
#         ("fdssdfs", "Некорректный номер карты"),
#     ],
# )
# def test_get_mask_card_number(card_number: int | str, expected_result: str):
#     assert get_mask_card_number(card_number) == expected_result
