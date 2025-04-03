import pytest
from src.decorators import log


@log()
def successful_function():
    return "Успешное выполнение"


@log()
def failing_function():
    raise ValueError("Произошла ошибка")


def test_successful_function(capsys):
    result = successful_function()
    captured = capsys.readouterr()
    assert "Успешное выполнение" in result
    assert "Функция successful_function началась в" in captured.out
    assert "Функция successful_function завершилась в" in captured.out


def test_failing_function(capsys):
    with pytest.raises(ValueError):
        failing_function()
    captured = capsys.readouterr()
    assert "Ошибка в failing_function: Произошла ошибка" in captured.out
