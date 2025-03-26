import json
import os



def parse_data(path: str) -> list:
    """Функция читает json файл, если файл пустой или не найден возвращает пустую строку"""
    try:
        with open(path, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)
            if type(data) is list:
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    print(parse_data(path))

