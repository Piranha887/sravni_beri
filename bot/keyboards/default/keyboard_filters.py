# Импорт необходимых модулей и классов
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Определение функции для создания клавиатуры фильтров
def keyboard_filters():
    # Создание объекта клавиатуры с заданными кнопками
    keyboard_filter = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton('\U0001f465 Количество игроков'), KeyboardButton('\U0001f522 Возраст')],
            [KeyboardButton('\U0001f4c5 Год выпуска'), KeyboardButton('\u2699 Издатель')],
            [KeyboardButton('\U0001f519 Главное меню')]
        ],
        resize_keyboard=True  # Параметр, определяющий автоматическое изменение размера клавиатуры
    )
    return keyboard_filter  # Возврат созданной клавиатуры
