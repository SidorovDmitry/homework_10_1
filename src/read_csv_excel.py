import os
import csv
import pandas as pd


file_path_csv = os.path.join(os.path.dirname(__file__), "../data", "transactions.csv")
file_path_excel = os.path.join(os.path.dirname(__file__), "../data", "transactions_excel.xlsx")


def read_csv_file(file_path, delimiter):
    """Функция для считывания финансовых операций из CSV файла и возврата списка словарей."""
    result = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=delimiter)  # Читаем как словари через библиотеку CSV
            for row in reader:
                result.append(row)
        return result

    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return []


# print(read_csv_file(file_path_csv,";")) # Для проверки работы функции


def read_excel_file(file_path):
    """Функция для считывания финансовых операций из XLSX-файла и возврата списка словарей."""
    try:

        df = pd.read_excel(file_path)  # Читаем Excel файл
        transaction_list = df.to_dict(orient="records")  # Преобразуем DataFrame в список словарей
        return transaction_list

    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


# print(read_excel_file(file_path_excel)) # Для проверки работы функции
