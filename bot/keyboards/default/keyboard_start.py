from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="\U0001f4d6 Библиотека"),
            KeyboardButton(text="\U0001f9ee Фильтры")
        ],
        [
            KeyboardButton(text="\U0001f4dc Описание"),
            KeyboardButton(text="\U0001f50e Анализ"),
            KeyboardButton(text="\U0001f4de Контакты")
        ],

    ], resize_keyboard=True
)

