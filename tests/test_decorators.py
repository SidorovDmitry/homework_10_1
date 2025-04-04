import pytest
from src.decorators import log


@log()
def successful_function():
    """Пример функции, которая успешно выполняется"""

    return "Успешное выполнение"


@log()
def failing_function():
    """Пример функции, которая вызывает исключение"""

    raise ValueError("Произошла ошибка")


def test_successful_function(capsys):
    """Тест для проверки успешного выполнения функции и корректной записи логов"""

    result = successful_function()
    captured = capsys.readouterr()
    assert "Успешное выполнение" in result
    assert "Функция successful_function началась в" in captured.out
    assert "Функция successful_function завершилась в" in captured.out


def test_failing_function(capsys):
    """Тест для проверки обработки исключения в функции и корректной записи логов"""

    with pytest.raises(ValueError):
        failing_function()
    captured = capsys.readouterr()
    assert "Ошибка в failing_function: Произошла ошибка" in captured.out
