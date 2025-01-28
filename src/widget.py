from src.masks import get_mask_account


def get_mask_account(score_or_card: str) -> str:
    """Функция, которая принимает на вход номер карты или счета и возвращает их маску"""
    score = "Счет"
    if score in score_or_card:
        return f"Счет **{score_or_card[-4:]}"
    else:
        list_number_card = score_or_card.split()
        name_card = ""
        number_card = ""
        for i in list_number_card:
            if i.isalpha():
                name_card += i
            elif i.isdigit():
                number_card += i
                return f"{(name_card)} {number_card[:4]} {number_card[6:8]}** **** {number_card[-4:]}"


def get_date(date_time: str) -> str:
    """Функция, которая принимает на вход строку с датой и временем и возвращает строку с датой"""
    return f"{date_time[8:10]}.{date_time[5:7]}.{date_time[:4]}"


print(get_mask_account("Visa Classic 6831982476737658"))
print(get_mask_account("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
