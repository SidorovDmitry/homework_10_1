import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_amount(transactions_finance, to_currency="RUB"):
    """Функция конвертации валют в другую валюту, по умолчанию конвертирует в RUB"""

    value = float(transactions_finance["operationAmount"]["amount"])
    from_currency = transactions_finance["operationAmount"]["currency"]["code"]

    if from_currency == to_currency:
        return value

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={value}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        status_code = response.status_code

        if status_code == 200:
            return response.json()["result"]
        else:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
            return 0.0
    except requests.exceptions.RequestException :
        print("Произошла ошибка, видимо в коде некорректные данные")
        return 0.0


# # Пример использования функции
# transactions_finance = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#         "amount": "0",
#         "currency": {
#             "code": "USD"
#         }
#     }
# }
#
# converted_amount = convert_amount(transactions_finance)
# print(converted_amount)
