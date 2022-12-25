from aiogram.types import ReplyKeyboardMarkup


def keyboard_analyse():
    # noinspection PyTypeChecker
    keyboard_analyse = ReplyKeyboardMarkup(
        keyboard=[
            ['Гистограмма "\U0001f465 Количество игроков"', 'Гистограмма "\U0001f522 Возраст"'],
            ['Гистограмма "\U0001f4c5 Год выпуска"', 'Гистограмма "\u2699 Издатель"'],
            ['\U0001f519 Главное меню']
        ], resize_keyboard=True
    )

    return keyboard_analyse