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
* generator.py: Модуль
который содержит функции для работы с массивами транзакций.
* utils.py: Модуль чтения для JSON файла из директории data в корне проекта
* external_api.py: Содержит функцию для конвертации валют с помощью внешнего API 
* decorators.py: Декоратор логирования выполнения функций с выводом в файл или консоль
* sorting_by_value.py: Модуль сортировки по параметрам
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
*Генерирует номера карт в заданном диапазоне*
```
def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    
    for num in range(start, end + 1):
        yield f"{num:016d}"
        
for card_number in card_number_generator(123456789012345, 123456789012349):
    print(card_number)
```
Декоратор для логирования работы функций

## Структура проекта

```
my_poetry__project_1/
├── data/                      # Папка с данными
├── htmlcov/                   # Отчёты coverage.py
├── src/                       # Исходный код
│   ├── __init__.py            # Пакетный файл
│   ├── decorators.py          # Декораторы
│   ├── external_apl.py        # Внешние API-интеграции
│   ├── generators.py          # Генераторы
│   ├── masks.py               # Маски данных
│   ├── sorting_by_value.py    # Модуль сортировки по параметрам
│   ├── processing.py          # Обработка данных
│   ├── utils.py               # Вспомогательные утилиты
│   └── widget.py              # Виджеты
├── tests/                     # Тесты
│   ├── __init__.py
│   ├── conftest.py            # Фикстуры pytest
│   ├── test_decorators.py
│   ├── test_external_apl.py
│   ├── test_sorting_by_value.py 
│   ├── test_generators.py
│   ├── test_masks.py
│   ├── test_processing.py
│   ├── test_titls.py
│   └── test_widget.py
├── .coverage                  # Файл coverage
├── .env                       # Переменные окружения
├── .env.example.py            # Шаблон .env
├── .flake8                    # Конфиг flake8
├── .gitignore                 # Игнорируемые файлы Git
├── main.py                    # Главный скрипт
├── poetry.lock                # Лок-файл Poetry
├── pyproject.toml             # Конфигурация Poetry
└── README.md                  # Документация                 
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

 