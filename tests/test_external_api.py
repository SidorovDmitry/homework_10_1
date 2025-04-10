from unittest.mock import Mock, patch

import requests

from src.external_api import convert_amount


def test_convert_amount_success():
    transactions_finance = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    # Создаем макет для requests.get()
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 90.0}

    # Используем patch для замены requests.get() на наш макет
    with patch("requests.get", return_value=mock_response):
        result = convert_amount(transactions_finance)

    # Проверяем, что результат совпадает с ожидаемым
    assert result == 90.0, "Результат не совпадает с ожидаемым"


def test_convert_amount_failure():
    transactions_finance = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    # Создаем макет для requests.get() с ошибкой
    mock_response = Mock()
    mock_response.status_code = 404

    # Используем patch для замены requests.get() на наш макет
    with patch("requests.get", return_value=mock_response):
        result = convert_amount(transactions_finance)

    # Проверяем, что функция возвращает None при ошибке
    assert result is None, "Функция не вернула None при ошибке"


def test_convert_amount_exception():
    transactions_finance = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    # Используем patch для имитации исключения RequestException
    with patch("requests.get", side_effect=requests.exceptions.RequestException):
        result = convert_amount(transactions_finance)

    # Проверяем, что функция возвращает None при исключении
    assert result is None, "Функция не вернула None при исключении"


if __name__ == "__main__":
    test_convert_amount_success()
    test_convert_amount_failure()
    test_convert_amount_exception()
    print("Все тесты пройдены успешно")
