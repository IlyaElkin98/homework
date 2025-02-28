def get_mask_card_number(number_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    if 0 < len(number_card) < 16:
        return "Неправильно набран номер карты. Проверьте правильность ввода"
    elif len(number_card) > 16:
        return "Неправильно набран номер карты. Проверьте правильность ввода"
    elif len(number_card) == 0:
        return "Пустая строка"
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:17]}"


def get_mask_account(account_mask: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    if 0 < len(account_mask) < 20:
        return "Неправильно набран номер счета. Проверьте правильность ввода"
    elif len(account_mask) > 20:
        return "Неправильно набран номер счета. Проверьте правильность ввода"
    elif len(account_mask) == 0:
        return "Пустая строка"
    return f"**{account_mask[-4:]}"


print(get_mask_card_number("number_card"))
print(get_mask_account("1234567890123"))
