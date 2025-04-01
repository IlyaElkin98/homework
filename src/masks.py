import logging

logger = logging.getLogger("masks.log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""
    logger.info("Получение данных о карте")
    if number_card.isdigit() == bool(0):
        logger.error("Номер карты должен состоять только из цифр ")
        return "Номер карты должен состоять только из цифр"
    elif len(number_card) == 16:
        logger.info("Номер карты успешно замаскирован")
        return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:17]}"
    elif len(number_card) != 16:
        logger.error("Номер карты должен состоять из 16 цифр")
        return "Неправильно набран номер карты. Проверьте правильность ввода"


def get_mask_account(account_mask: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает его маску"""
    logger.info("Получение данных о счёте")
    if account_mask.isdigit() == bool(0):
        logger.error("Номер счёта должен состоять только из цифр")
        return "Номер счёта должен состоять только из цифр"
    elif len(account_mask) == 20:
        logger.info("Номер счёт замаскирован")
        return f"**{account_mask[-4:]}"
    elif len(account_mask) != 20:
        logger.error("Номер счёт должен состоять из 20 цифр")
        return "Неправильно набран номер счета. Проверьте правильность ввода"


print(get_mask_card_number("2000546482431542"))
print(get_mask_account("20005464824315427564"))
