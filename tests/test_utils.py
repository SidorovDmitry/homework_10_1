from unittest.mock import Mock, patch

from src.utils import read_file


def test_read_file_success():
    # Создаем макет для open()
    mock_file = Mock()
    mock_file.read.return_value = '["some", "data"]'  # Пример данных в формате JSON
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock(return_value=False)

    # Используем patch для замены open() на наш макет
    with patch("builtins.open", return_value=mock_file):
        result = read_file()

    # Проверяем, что данные были успешно прочитаны и декодированы
    assert result == ["some", "data"], "Данные не совпадают с ожидаемыми"


def test_read_file_file_not_found():
    # Используем patch для имитации ошибки FileNotFoundError
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_file()

    # Проверяем, что функция возвращает пустой список при ошибке
    assert result == [], "Функция не вернула пустой список при ошибке FileNotFoundError"


def test_read_file_json_decode_error():
    # Создаем макет для open() с некорректными данными JSON
    mock_file = Mock()
    mock_file.read.return_value = "not json data"
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock(return_value=False)

    # Используем patch для замены open() на наш макет
    with patch("builtins.open", return_value=mock_file):
        result = read_file()

    # Проверяем, что функция возвращает пустой список при ошибке декодирования JSON
    assert result == [], "Функция не вернула пустой список при ошибке JSONDecodeError"


def test_read_file_not_list():
    # Создаем макет для open() с данными, которые не являются списком
    mock_file = Mock()
    mock_file.read.return_value = '{"key": "value"}'
    mock_file.__enter__ = Mock(return_value=mock_file)
    mock_file.__exit__ = Mock(return_value=False)

    # Используем patch для замены open() на наш макет
    with patch("builtins.open", return_value=mock_file):
        result = read_file()

    # Проверяем, что функция возвращает пустой список, если данные не являются списком
    assert result == [], "Функция не вернула пустой список, если данные не являются списком"


if __name__ == "__main__":
    test_read_file_success()
    test_read_file_file_not_found()
    test_read_file_json_decode_error()
    test_read_file_not_list()
    print("Все тесты пройдены успешно")
