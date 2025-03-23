import json
import os

import requests

api_key = "40e75ee8e0694a4ab040e335fb3a1fd7"


def parse_data(path: str) -> list:
    """Функция читает json файл, если файл пустой или не найден возвращает пустую строку"""
    try:
        with open(path, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    print(parse_data(path))


def transaction_api(data: dict) -> float:
    """Функция реализующая конвертацию валюты"""
    amount = data.get("operationAmount", {}).get("amount")
    currency_code = data.get("operationAmount", {}).get("currency", {}).get("code")

    if currency_code == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        payload = {}
        headers = {"apikey": "3zMA6Nf74bY73xgyUL4AqqgW5tLKwoE4"}
        response = requests.get(url, headers=headers)

        result = response.text
        return result


if __name__ == "__main__":
    print(
        transaction_api(
            {
                "id": 558167602,
                "state": "EXECUTED",
                "date": "2019-04-12T17:27:27.896421",
                "operationAmount": {"amount": "43861.89", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 73654108430135874305",
                "to": "Счет 89685546118890842412",
            }
        )
    )
