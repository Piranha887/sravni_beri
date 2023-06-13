from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_manufactory():
    query_manufactories = [manufacture.manufacture_buttons for manufacture in Buttons.select()]

    lines_filters_manufactory: List[List[Any]] = list(partition(query_manufactories, 4))

    keyboard_buttons = []
    for line in lines_filters_manufactory:
        keyboard_buttons.append(line)

    keyboard_buttons.append(['\U0001f519 Фильтры'])

    keyboard_filters_manufactures = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True)
    return keyboard_filters_manufactures
