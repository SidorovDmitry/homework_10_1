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


# Тесты для корректных форматов даты
@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("1999-12-31T23:59:59", "31.12.1999"),
        ("2000-01-01T00:00:00", "01.01.2000"),
        ("2023-02-28T15:30:45", "28.02.2023"),
    ],
)
def test_valid_date_formats(date_string, expected):
    """Тестирование корректных форматов даты"""
    assert get_date(date_string) == expected


# Дополнительные тесты для граничных случаев
def test_whitespace_string():
    """Тестирование строки с пробелами"""
    with pytest.raises(ValueError):
        get_date("   ")


def test_partial_date_string():
    """Тестирование неполной строки даты"""
    with pytest.raises(ValueError):
        get_date("2024-03")


# Тест для проверки сохранения формата
def test_output_format():
    """Проверка что выходной формат всегда ДД.ММ.ГГГГ"""
    result = get_date("2024-12-01T00:00:00")
    assert result == "01.12.2024"
    assert len(result.split(".")) == 3
    assert all(part.isdigit() for part in result.split("."))
