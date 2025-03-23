import pytest

# Фикстуры для функции mask_account_card
# Фикстура для корректного номера счета
@pytest.fixture
def valid_account_number():
    return "Счет 12345678901234567890"

# Фикстура для корректного номера карты
@pytest.fixture
def valid_card_number():
    return "Visa Platinum 1234567890123456"

# Фикстура для некорректного номера счета (неправильная длина)
@pytest.fixture
def invalid_account_number():
    return "Счет 123"

# Фикстура для некорректного номера карты (неправильная длина)
@pytest.fixture
def invalid_card_number():
    return "Visa Platinum 123456789012345"

# Фикстура для пустой строки
@pytest.fixture
def empty_string():
    return ""

# Фикстура для строки без номера
@pytest.fixture
def no_number_string():
    return "Счет "

# Фикстуры для функции get_date
# Фикстура для корректной даты
@pytest.fixture
def correct_date_string():
    return "2024-03-11T02:26:18.671407"

# Фикстура для некорректной даты (отсутствует время)
@pytest.fixture
def incorrect_date_string_no_time():
    return "11-03-2024"

# Фикстура для некорректной даты (неправильный разделитель" ")
@pytest.fixture
def incorrect_date_string_wrong_separator():
    return "11.03.2024 02:26:18"

# Фикстура для некорректной даты (лишние символы в конце)
@pytest.fixture
def incorrect_date_string_extra_chars():
    return "2024-03-11T02:26:18.671407Z"

# Фикстура для некорректной даты (нечисловые символы)
@pytest.fixture
def incorrect_date_string_non_numeric():
    return "2024-03-ABT02:26:18.671407"

# Фикстура для некорректной даты (неправильный разделитель ":")
@pytest.fixture
def incorrect_date_string_wrong_delimiter():
    return "2024-03-11X02:26:18.671407"

# Фикстура для некорректной даты (слишком много частей)
@pytest.fixture
def incorrect_date_string_too_many_parts():
    return "2024-03-11T02:26:18.671407XYZ"

# Фикстура для некорректной даты (неверный месяц)
@pytest.fixture
def incorrect_date_string_invalid_month():
    return "2024-13-11T02:26:18.671407"
