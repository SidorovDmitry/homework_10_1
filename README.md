# Проект "*Банковских операции клиента*"
 
## Описание
#### Этот проект предоставляет инструменты для работы с транзакциями, включая фильтрацию и сортировку, а так же маскировку номера карт/счетов.


## Установка:
1. Убедитесь, что у вас установлен Python 3.13 или выше.
2. Установите Poetry, если он еще не установлен:
```
pip install poetry
```
3. Клонируйте репозиторий:
```
git clone git@github.com:SidorovDmitry/homework_10_1.git
```
4. Перейдите в директорию проекта:
```
cd homework_10_1
```
5. Установите зависимостис помощью Poetry:
```
poetry install
```
6. Активируйте виртуальное окружение:
```
poetry shell
```

## Использование:

Основные модули
* masks.py: Содержит функции для маскировки номеров карт и счетов.
* processing.py: Содержит функции для фильтрации и сортировки транзакций.
* widget.py: Основной модуль для взаимодействия с пользователем.

Пример использования:

*Фильтрация транзакций по state*
```
from src.processing import filter_by_state

transactions = [
    {"id": 1, "state": "EXECUTED", "amount": 100},
    {"id": 2, "state": "PENDING", "amount": 200},
    {"id": 3, "state": "EXECUTED", "amount": 300},
]

filtered_transactions = filter_by_state(transactions)
print(filtered_transactions)
```
*Сортировка транзакций по дате*
```
from src.processing import sort_by_date

transactions = [
    {"id": 1, "date": "2024-03-11T02:26:18.671407", "amount": 100},
    {"id": 2, "date": "2024-02-15T12:30:45.123456", "amount": 200},
    {"id": 3, "date": "2024-04-01T08:15:30.987654", "amount": 300},
]

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)
```
## Структура проекта

```
my_poetry_project_1/                     # Корневая директория проекта
├── htmlcov/                             # Отчеты о покрытии кода тестами (генерируется coverage)
├── src/                                 # Основная директория с исходным кодом
│   ├── __init__.py                      # Делает директорию `src` пакетом Python
│   ├── masks.py                         # Модуль для работы с масками данных
│   ├── processing.py                    # Модуль для обработки данных
│   └── widget.py                        # Модуль с виджетами (например, для GUI)
├── tests/                               # Директория с тестами
│   ├── __init__.py                      # Делает директорию `tests` пакетом Python
│   ├── conftest.py                      # Настройки pytest (например, фикстуры)
│   ├── test_masks.py                    # Тесты для модуля masks.py
│   ├── test_processing.py               # Тесты для модуля processing.py
│   └── test_widget.py                   # Тесты для модуля widget.py
├── .coverage                            # Данные о покрытии кода тестами (генерируется coverage)
├── .flake8                              # Конфигурация для линтера flake8
├── .gitignore                           # Файл для игнорирования ненужных файлов в Git
├── main.py                              # Основной исполняемый файл проекта
├── poetry.lock                          # Файл с точными версиями зависимостей (генерируется Poetry)
├── pyproject.toml                       # Конфигурация Poetry (зависимости, настройки проекта)
└── README.md                            # Файл с описанием проекта
```
## Зависимости
Зависимости проекта управляются через Poetry. Они перечислены в файле `pyproject.toml`

## Тестирование
Для запуска тестов используйте команду: `paytest`

Для проверки покрытия кода тестами используйте команду: `pytest --cov`

## Документация:
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Dmitrii+Sidorov)](https://git.io/typing-svg)

 