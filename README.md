# Учебный проект 10.1

## Описание:

Учебный проект 10.1 - проект созданный для сортировки данных банковских операций клиента

## Установка:

1. Клонируйте удаленный репозиторий:
```
https://github.com/IlyaElkin98/homework_10_1.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

