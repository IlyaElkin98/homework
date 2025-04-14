import json
import os
import re
from collections import Counter



def search_by_string(operations_list: list[dict], search_string: str) -> list[dict]:
    """Поиск в списке операций по заданной строке. Возвращает список операций с подходящим описанием"""
    try:
        with open(operations_list, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)
            operations_found = []
            pattern = re.compile(search_string)
            for operation in data:
                descr = operation.get("description", "")
                if pattern.search(descr):
                    operations_found.append(operation)
            return operations_found
    except FileNotFoundError:
        return "Файл operations.json - не найден"
    except json.JSONDecodeError:
        return "Данные JSON недействительны"

print(search_by_string("data/operations.json", "Перевод"))



def bank_categories(operations_list: list[dict], list_categories: list) -> dict:
    """Функция подсчета операций по заданным пользователем категориям. Возвращает словарь с названиями категорий и их количеством"""
    list_ctg = []
    with open(operations_list, "r", encoding="utf-8") as json_data:
        data = json.load(json_data)
        for operation in data:
            if len(operation.get("description", "")) != 0:
                list_ctg.append(operation.get("description"))
                counter = Counter(list_ctg)
        return dict(counter)

print(bank_categories("data/operations.json", []))
