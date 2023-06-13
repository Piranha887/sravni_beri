from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_filter_main_menu():
    keyboard_fil_mm = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton('\U0001f519 Фильтры')],
            [KeyboardButton('\U0001f519 Главное меню')]
        ],
        resize_keyboard=True
    )
    return keyboard_fil_mm
