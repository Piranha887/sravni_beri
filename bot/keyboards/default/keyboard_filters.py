from aiogram.types import ReplyKeyboardMarkup


def keyboard_filters():
    # noinspection PyTypeChecker
    keyboard_filter = ReplyKeyboardMarkup(
        keyboard=[
            ['\U0001f465 Количество игроков', '\U0001f522 Возраст'],
            ['\U0001f4c5 Год выпуска', '\u2699 Издатель'],
            ['\U0001f519 Главное меню']
        ], resize_keyboard=True
    )

    return keyboard_filter
