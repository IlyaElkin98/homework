import pytest


@pytest.fixture
def date_1():
    return "11.03.2024"


@pytest.fixture
def date_2():
    return "Пустая строка!"


@pytest.fixture
def date_3():
    return "21.11.2023"


@pytest.fixture
def date_4():
    return "Во входной строке отсутсвует дата"
