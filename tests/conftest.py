import pytest


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
