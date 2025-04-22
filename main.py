from config import PATH_TO_CSV, PATH_TO_EXCEL, PATH_TO_JSON
from src.read_csv_excel import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.sorting_by_value import count_operations_by_category, filter_transactions
from src.utils import read_file
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency



def format_transaction(transaction: dict) -> str:
    """Форматирует транзакцию для вывода с валютой"""
    try:
        # Основные данные
        date = get_date(transaction.get("date", ""))
        description = transaction.get("description", "Описание отсутствует")

        # Обработка карт/счетов
        from_account = mask_account_card(str(transaction["from"])) if "from" in transaction and str(
            transaction["from"]) != "nan" else ""
        to_account = mask_account_card(str(transaction.get("to", "Получатель не указан")))

        # Получаем сумму и валюту
        amount = "не указана"
        currency = ""

        # Проверяем разные варианты структуры суммы
        if "amount" in transaction and transaction["amount"] is not None:
            amount = transaction["amount"]
            # Пробуем получить валюту из разных возможных полей
            currency = transaction.get("currency",
                                       transaction.get("currency_code",
                                                       transaction.get("currency_name", "")))
        elif "operationAmount" in transaction:
            op_amount = transaction["operationAmount"]
            if isinstance(op_amount, dict):
                amount = op_amount.get("amount", "не указана")
                curr_info = op_amount.get("currency", {})
                if isinstance(curr_info, dict):
                    currency = curr_info.get("code", "")
                else:
                    currency = str(curr_info)

        # Форматируем сумму
        try:
            if isinstance(amount, (int, float)):
                amount_display = f"{amount:,.2f}".replace(",", " ").replace(".00", "")
            else:
                amount_display = str(amount).strip()
        except Exception:
            amount_display = "не указана"

        # Приводим валюту к стандартному виду
        currency = currency.upper() if isinstance(currency, str) else ""
        if currency == "RUB":
            currency = "RUB"  # Или "₽" если хотите символ рубля
        elif currency == "USD":
            currency = "USD"  # Или "$"
        elif currency == "EUR":
            currency = "EUR"  # Или "€"

        # Формируем результат
        result = f"{date} {description}\n"
        if from_account:
            result += f"{from_account} -> "
        result += f"{to_account}\n"
        result += f"Сумма: {amount_display} {currency}" if currency else f"Сумма: {amount_display}"

        return result

    except Exception as e:
        print(f"Ошибка форматирования транзакции: {e}")
        return f"Не удалось отформатировать транзакцию: {transaction}"

def show_statistics(transactions):
    """Выводит статистику по операциям"""
    common_categories = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод со счета на счет",
        "Открытие вклада",
        "Пополнение счета",
    ]

    stats = count_operations_by_category(transactions, common_categories)
    print("\nСтатистика операций по категориям:")
    for category, count in stats.items():
        print(f"{category}: {count}")


def main():
    print("""
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)

    # Выбор файла
    while True:
        file_type = input("Выберите номер операции: ").strip()
        if file_type in ("1", "2", "3"):
            file_names = {"1": "JSON", "2": "CSV", "3": "XLSX"}
            print(f"\nДля обработки выбран {file_names[file_type]}-файл.")
            break
        else:
            print("Пожалуйста, введите корректный номер: 1, 2 или 3")

    # Загрузка данных
    transactions = []
    try:
        if file_type == "1":
            transactions = read_file(PATH_TO_JSON)
        elif file_type == "2":
            transactions = read_csv_file(PATH_TO_CSV)
        elif file_type == "3":
            transactions = read_excel_file(PATH_TO_EXCEL)
    except Exception as e:
        print(f"\nОшибка при загрузке файла: {e}")
        return

    # Фильтрация по статусу
    while True:
        print("\nВведите статус для фильтрации:")
        print("Доступные статусы: EXECUTED, CANCELED, PENDING")
        state = input("Ваш выбор: ").upper().strip()

        if state in ("EXECUTED", "CANCELED", "PENDING"):
            try:
                filtered = filter_by_state(transactions, state)
                if not filtered:
                    print(f"\nНет операций со статусом '{state}'")
                    return
                transactions = filtered
                print(f"\nНайдено {len(transactions)} операций со статусом '{state}'")
                break
            except ValueError as e:
                print(f"\nОшибка при фильтрации: {e}")
                return
        else:
            print(f'\nСтатус операции "{state}" недоступен')


    # Сортировка по дате
    while True:
        sort_choice = input("\nОтсортировать операции по дате? (да/нет): ").lower().strip()
        if sort_choice in ("да", "нет"):
            break

    if sort_choice == "да":
        while True:
            sort_order = input("Сортировать по возрастанию или убыванию? ").lower().strip()
            if sort_order == "возрастанию":
                transactions = sort_by_date(transactions)
                break
            elif sort_order == "убыванию":
                transactions = sort_by_date(transactions, reverse=True)
                break
            else:
                print("Пожалуйста, введите 'возрастанию' или 'убыванию'")

    # Фильтрация по ключевому слову
    while True:
        filter_word = input("\nФильтровать по слову в описании? (да/нет): ").lower().strip()
        if filter_word in ("да", "нет"):
            break

    if filter_word == "да":
        keyword = input("Введите ключевое слово (например: Перевод, Открытие): ").strip()
        transactions = filter_transactions(transactions, keyword)
        if not transactions:
            print("Нет операций с таким ключевым словом")
            return

    # Фильтрация по валюте
    while True:
        currency_choice = input("\nФильтровать по валюте? (да/нет): ").lower().strip()
        if currency_choice in ("да", "нет"):
            break

    if currency_choice == "да":
        while True:
            currency = input("Введите валюту (RUB, USD, EUR): ").upper().strip()
            if currency in ("RUB", "USD", "EUR"):
                transactions = list(filter_by_currency(transactions, currency))
                if not transactions:
                    print(f"Нет операций в валюте {currency}")
                    return
                break
            else:
                print("Неверная валюта. Допустимые значения: RUB, USD, EUR")

    # Вывод результатов
    print("\nИтоговый список транзакций:\n")
    print(f"Всего операций: {len(transactions)}\n")

    for i, transaction in enumerate(transactions, 1):
        print(f"Операция #{i}")
        print(format_transaction(transaction))
        print("-" * 50)

    if transactions:
        show_statistics(transactions)


if __name__ == "__main__":
    main()
