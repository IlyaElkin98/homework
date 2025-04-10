import csv
import os
from typing import Any

import pandas as pd


def transaction_csv(file_path: str) -> list[str | Any] | str:
    """Функция считывания финансовых операций из CSV файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as f_csv:
            reader = csv.DictReader(f_csv, delimiter=";")
            for data in reader:
                return list(data)
    except ValueError:
        return "Данные отсутствуют или не соответствуют формату"
    except FileNotFoundError:
        return "Файл не найден"
    except TypeError:
        return "Неверный тип данных"


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
    print(transaction_csv('data/transactions.csv'))


def transaction_xlsx(file_path_xlsx: str) -> list:
    """Функция считывания финансовых операций из Excel файла"""
    try:
        xlsx = pd.read_excel(file_path_xlsx, engine="openpyxl")
        xlsx_dict = xlsx.to_dict(orient="records")
        return xlsx_dict
    except ValueError:
        return "Данные отсутствуют или не соответствуют формату"
    except FileNotFoundError:
        return "Файл не найден"


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
    print(transaction_xlsx('data/transactions_excel.xlsx'))
