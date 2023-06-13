from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_main_menu():
    keyboard_mm = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton('\U0001f519 Главное меню')]
        ],
        resize_keyboard=True
    )
    return keyboard_mm
