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
├── src/
│   ├── __init__.py               # Пустой файл для создания пакета
│   ├── masks.py                  # Функции для маскировки карт и счетов
│   ├── processing.py             # Функции для обработки транзакций
│   ├── widget.py                 # Основной модуль для взаимодействия с пользователем
│   └── tests/                    # Папка для тестов (пока пустая)
│       └── __init__.py           # Пустой файл для создания пакета
├── .flake8                       # Конфигурация Flake8 (линтер)
├── .gitignore                    # Файл для игнорирования файлов в Git
├── main.py                       # Основной скрипт для запуска проекта
├── poetry.lock                   # Файл блокировки Poetry
├── pyproject.toml                # Конфигурация Poetry
└── README.md                     # Описание проекта
```
## Зависимости
Зависимости проекта управляются через Poetry. Они перечислены в файле `pyproject.toml`

## Тестирование
Для запуска тестов используйте команду:

## Документация:
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Dmitrii+Sidorov)](https://git.io/typing-svg)

 