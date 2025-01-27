number_card = input()
account_mask = input()


def get_mask_card_number(number_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:17]}"


def get_mask_account(account_mask: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    return f"**{account_mask[-4:]}"


print(get_mask_card_number(number_card))
print(get_mask_account(account_mask))