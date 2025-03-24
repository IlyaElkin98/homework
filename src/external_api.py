import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

def transaction_api(data: dict) -> float:
    """Функция реализующая конвертацию валюты"""
    amount = data.get("operationAmount", {}).get("amount")
    currency_code = data.get("operationAmount", {}).get("currency", {}).get("code")

    if currency_code == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)

        result = response.json()
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
