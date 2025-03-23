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

