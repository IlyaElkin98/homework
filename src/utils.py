import json
import os
import logging

logger = logging.getLogger('utils.log')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def parse_data(path_file: str) -> list:
    """Функция читает json файл, если файл пустой или не найден возвращает пустую строку"""
    try:
        logger.info(f'Выполняется запись данных в файл operations.json')
        with open(path_file, "r", encoding='utf-8') as json_data:
            data = json.load(json_data)
            if type(data) is list:
                return data
            else:
                return []
    except FileNotFoundError:
        file_not_found = 'Файл не найден'
        logger.error(file_not_found)
        return []
    except json.JSONDecodeError:
        json_code_error = 'Данные JSON недействительны'
        logger.error(json_code_error)
        return []


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    print(parse_data(path))

