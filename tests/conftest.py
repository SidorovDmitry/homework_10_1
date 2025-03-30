import pytest


# Фикстура, возвращающая список тестовых данных для get_mask_card_number
@pytest.fixture
def card_number_test_data():
    return [
        ("1234567812345678", "1234 56** **** 5678"),  # Корректный номер карты
        ("12345678", "Некорректный номер карты"),  # Слишком короткий номер
        ("123456781234567812", "Некорректный номер карты"),  # Слишком длинный номер
        ("123456781234567A", "Некорректный номер карты"),  # Нечисловые символы
        ("", "Некорректный номер карты"),  # Пустая строка
    ]


# Фикстура, возвращающая список тестовых данных для get_mask_account
@pytest.fixture
def account_number_test_data():
    return [
        ("12345678901234567890", "**7890"),  # Корректный номер счёта
        ("1234", "Некорректный номер счёта"),  # Слишком короткий номер
        ("fdssdfs", "Некорректный номер счёта"),  # Нечисловые символы
        ("", "Некорректный номер счёта"),  # Пустая строка
    ]


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


# Фикстура для тестовых данных filter_by_state
@pytest.fixture
def filter_by_state_data():
    return [
        (
            [  # Входные данные
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
                {"state": "PENDING", "date": "2024-01-02", "amount": 200},
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 300},
            ],
            "EXECUTED",  # Параметр state
            [  # Ожидаемый результат
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 300},
            ],
        ),
        (
            [  # Входные данные
                {"state": "PENDING", "date": "2024-01-01", "amount": 100},
                {"state": "CANCELED", "date": "2024-01-02", "amount": 200},
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 300},
            ],
            "PENDING",  # Параметр state
            [  # Ожидаемый результат
                {"state": "PENDING", "date": "2024-01-01", "amount": 100},
            ],
        ),
        (
            [  # Входные данные
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
                {"state": "EXECUTED", "date": "2024-01-02", "amount": 200},
            ],
            "CANCELED",  # Параметр state
            [],  # Ожидаемый результат (пустой список)
        ),
    ]


# Фикстура для тестовых данных sort_by_date
@pytest.fixture
def sort_by_date_data():
    return [
        (
            [  # Входные данные
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 200},
                {"state": "EXECUTED", "date": "2024-01-02", "amount": 300},
            ],
            True,  # Параметр reverse (по умолчанию)
            [  # Ожидаемый результат (по убыванию)
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 200},
                {"state": "EXECUTED", "date": "2024-01-02", "amount": 300},
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
            ],
        ),
        (
            [  # Входные данные
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 200},
                {"state": "EXECUTED", "date": "2024-01-02", "amount": 300},
            ],
            False,  # Параметр reverse (по возрастанию)
            [  # Ожидаемый результат (по возрастанию)
                {"state": "EXECUTED", "date": "2024-01-01", "amount": 100},
                {"state": "EXECUTED", "date": "2024-01-02", "amount": 300},
                {"state": "EXECUTED", "date": "2024-01-03", "amount": 200},
            ],
        ),
    ]




# Фикстура с тестовыми данными для функций filter_by_currency и transaction_descriptions
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]