user_input = input()

def get_mask_account(account_mask: str) -> str:
    """Функция, которая принимает на вход номер карты или счета и возвращает его маску"""
    account = 'Счет'
    card = 'Visa Platinum'
    card_1 = 'Maestro'
    if account in account_mask:
        return f"**{account_mask[-4:]}"
    elif card in account_mask:
        return f'Visa Platinum {account_mask[14:18]} {account_mask[18:20]}** **** {account_mask[-4:]}'
    elif card_1 in account_mask:
        return f'Maestro {account_mask[8:12]} {account_mask[12:14]}** **** {account_mask[-4:]}'

print(get_mask_account(user_input))



