# Учебный проект 10.1

## Описание:

Учебный проект 10.2 - проект созданный для сортировки данных банковских операций клиента, 
также в проекте фунционирует тестирование ПО

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
Примеры параметризации тестов:

```python
from src.masks import get_mask_card_number, get_mask_account
import pytest

# Пример использования test_masks.py
@pytest.mark.parametrize(
    "number_card, masked_number",
    [
        ("2200240824255657", "2200 24** **** 5657"),
        ("220224245454820761", "Неправильно набран номер карты. Проверьте правильность ввода"),
        ("", "Пустая строка"),
    ],
)
def test_get_mask_card_number(number_card: str, masked_number: str) -> None:
    assert get_mask_card_number(number_card) == masked_number
```
Примеры хуков(фикстур):

```python
import pytest


# Пример использования conftest.py
@pytest.fixture
def date_1(time: str) -> str:
    return "11.03.2024"


@pytest.fixture
def date_2(time: str) -> str:
    return "Пустая строка!"


@pytest.fixture
def date_3(time: str) -> str:
    return "21.11.2023"


@pytest.fixture
def date_4(time: str) -> str:
    return "Во входной строке отсутсвует дата"
```
