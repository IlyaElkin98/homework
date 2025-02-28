import pytest

from src.widget import get_date, get_mask_account


@pytest.mark.parametrize(
    "score_or_card, total_result",
    [
        ("Счет 10203040506070809000", "Счет **9000"),
        ("MasterCard 1615823461215490", "MasterCard 1615 82** **** 5490"),
        ("", "Пустая строка"),
        ("VisaPlatinum 7000792289606361", "VisaPlatinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_get_mask_account(score_or_card: str, total_result: str) -> None:
    assert get_mask_account(score_or_card) == total_result


def test_get_date1(date_1: str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date2(date_2: str) -> None:
    assert get_date("") == "Пустая строка!"


def test_get_date3(date_3: str) -> None:
    assert get_date("21-11-2023T02:26:18.671407") == "21.11.2023"


def test_get_date4(date_4: str) -> None:
    assert get_date("46838347582758892") == "Во входной строке отсутствует дата"
