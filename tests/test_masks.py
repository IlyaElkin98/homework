import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, masked_number",
    [
        ("2200240824255657", "2200 24** **** 5657"),
        ("220224245454820761", "Неправильно набран номер карты. Проверьте правильность ввода"),
    ],
)
def test_get_mask_card_number(number_card: str, masked_number: str) -> None:
    assert get_mask_card_number(number_card) == masked_number


@pytest.mark.parametrize(
    "account_mask, masked_account",
    [
        ("12345678901234567890", "**7890"),
        ("12313545643879504078434", "Неправильно набран номер счета. Проверьте правильность ввода"),
    ],
)
def test_get_mask_account(account_mask: str, masked_account: str) -> None:
    assert get_mask_account(account_mask) == masked_account
