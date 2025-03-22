import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Корректные данные
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
        # Некорректные данные
        ("", pytest.raises(ValueError, match="Входная строка пустая")),
        ("MasterCard 1234567890", pytest.raises(ValueError, match="Некорректный формат карты")),
        ("Счет 1234567890", pytest.raises(ValueError, match="Некорректный формат счета")),
        ("Visa Platinum", pytest.raises(ValueError, match="Некорректный формат: отсутствует номер карты или счета")),
    ],
)
def test_mask_account_card(input_data: str, expected_output: str):
    """Тестирование функции mask_account_card с различными входными данными."""
    if isinstance(expected_output, str):
        # Проверяем корректные данные
        assert mask_account_card(input_data) == expected_output
    else:
        # Проверяем исключения для некорректных данных
        with expected_output:
            mask_account_card(input_data)


def test_correct_format(correct_date_string: str):
    assert get_date(correct_date_string) == "11.03.2024"


def test_incorrect_format_no_time(incorrect_date_string_no_time: str):
    assert get_date(incorrect_date_string_no_time) == "Некорректный формат даты"


def test_incorrect_format_wrong_separator(incorrect_date_string_wrong_separator: str):
    assert get_date(incorrect_date_string_wrong_separator) == "Некорректный формат даты"


def test_incorrect_format_extra_chars(incorrect_date_string_extra_chars: str):
    assert get_date(incorrect_date_string_extra_chars) == "Некорректный формат даты"


def test_incorrect_format_non_numeric(incorrect_date_string_non_numeric: str):
    assert get_date(incorrect_date_string_non_numeric) == "Некорректный формат даты"


def test_incorrect_format_wrong_delimiter(incorrect_date_string_wrong_delimiter: str):
    assert get_date(incorrect_date_string_wrong_delimiter) == "Некорректный формат даты"


def test_incorrect_format_too_many_parts(incorrect_date_string_too_many_parts: str):
    assert get_date(incorrect_date_string_too_many_parts) == "Некорректный формат даты"


def test_incorrect_format_invalid_month(incorrect_date_string_invalid_month: str):
    assert get_date(incorrect_date_string_invalid_month) == "Некорректный формат даты"
