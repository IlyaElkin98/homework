import csv
import os
import pandas as pd


def transaction_csv(file_path: str) -> list:
    """Функция считывания финансовых операций из CSV файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as f_csv:
            reader = csv.DictReader(f_csv, delimiter=";")
            for row in reader:
                print(row)
    except ValueError:
        return "Данные отсутствуют или не соответствуют формату"
    except FileNotFoundError:
        return "Файл не найден"
    except TypeError:
        return 'Неверный тип данных'


transaction_csv("data/transactions.csv")


def transaction_xlsx(file_path_xlsx):
    """Функция считывания финансовых операций из Excel файла"""
    try:
        path = "data/transactions_excel.xlsx"
        xlsx = pd.read_excel(path, engine="openpyxl")
        xlsx_dict = xlsx.to_dict()
        print(xlsx_dict)
    except ValueError:
        return "Данные отсутствуют или не соответствуют формату"
    except FileNotFoundError:
        return "Файл не найден"


transaction_xlsx("data/transactions_excel.xlsx")
