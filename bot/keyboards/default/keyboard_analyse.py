# Импорт необходимых модулей и классов
from aiogram.types import ReplyKeyboardMarkup


# Определение функции для создания клавиатуры анализа
def keyboard_analyse():
    # noinspection PyTypeChecker
    # Создание объекта клавиатуры с заданными кнопками
    keyboard_analyse = ReplyKeyboardMarkup(
        keyboard=[
            ['Гистограмма "\U0001f465 Количество игроков"', 'Гистограмма "\U0001f522 Возраст"'],
            ['Гистограмма "\U0001f4c5 Год выпуска"', 'Гистограмма "\u2699 Издатель"'],
            ['\U0001f519 Главное меню']
        ],
        resize_keyboard=True  # Параметр, определяющий автоматическое изменение размера клавиатуры
    )

    return keyboard_analyse  # Возврат созданной клавиатуры
