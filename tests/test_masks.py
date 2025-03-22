import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "account_number, expected_result",
    [
        (73654108430135874305, "**4305"),
        (1234567890123456, "**3456"),
        (12314323415, "**3415"),
        (1234, "**1234"),
        (123, "Некорректный номер счёта"),
        ("fdssdfs", "Некорректный номер счёта"),
        ("", "Некорректный номер счёта"),
    ],
)
def test_get_mask_account(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        (1234567812345678, "1234 56** **** 5678"),
        (0, "Некорректный номер карты"),
        (12345678, "Некорректный номер карты"),
        (123456781234567812, "Некорректный номер карты"),
        ("123456781234567A", "Некорректный номер карты"),
        ("", "Некорректный номер карты"),
        ("fdssdfs", "Некорректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result
