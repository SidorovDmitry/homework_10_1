import pytest

from src.widget import get_date, mask_account_card


# Тестирование функции mask_account_card с помощью фикстур.
def test_mask_account_card_valid_account(valid_account_number):
    result = mask_account_card(valid_account_number)
    assert result == "Счет **7890"


def test_mask_account_card_valid_card(valid_card_number):
    result = mask_account_card(valid_card_number)
    assert result == "Visa Platinum 1234 56** **** 3456"


def test_mask_account_card_invalid_account(invalid_account_number):
    with pytest.raises(ValueError):
        mask_account_card(invalid_account_number)


def test_mask_account_card_invalid_card(invalid_card_number):
    with pytest.raises(ValueError):
        mask_account_card(invalid_card_number)


def test_mask_account_card_empty_string(empty_string):
    with pytest.raises(ValueError):
        mask_account_card(empty_string)


def test_mask_account_card_no_number(no_number_string):
    with pytest.raises(ValueError):
        mask_account_card(no_number_string)


# Тестирование функции mask_account_card с помощью параметризации.
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


# Тестирование функции get_date с помощью фикстур.
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


# Параметризованный тест для функции get_date
@pytest.mark.parametrize(
    "date_string, expected_output",
    [
        # Корректные данные
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Корректная дата
        ("2023-12-31T23:59:59.999999", "31.12.2023"),  # Корректная дата (граничные значения)
        # Некорректные данные
        ("11-03-2024", "Некорректный формат даты"),  # Отсутствует время
        ("11.03.2024 02:26:18", "Некорректный формат даты"),  # Неправильный разделитель
        ("2024-03-11T02:26:18.671407Z", "Некорректный формат даты"),  # Лишние символы в конце
        ("2024-03-ABT02:26:18.671407", "Некорректный формат даты"),  # Нечисловые символы
        ("2024-03-11X02:26:18.671407", "Некорректный формат даты"),  # Неправильный разделитель между датой и временем
        ("2024-03-11T02:26:18.671407XYZ", "Некорректный формат даты"),  # Слишком много частей
        ("2024-13-11T02:26:18.671407", "Некорректный формат даты"),  # Неверный месяц
    ],
)
def test_get_date(date_string, expected_output):
    result = get_date(date_string)
    assert result == expected_output
