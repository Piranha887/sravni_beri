from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_year():
    query_years = [year.year_buttons for year in Buttons.select()]

    lines_filters_year: List[List[Any]] = list(partition(query_years, 3))

    keyboard_buttons = []
    for line in lines_filters_year:
        keyboard_buttons.append(line)

    keyboard_buttons.append(['\U0001f519 Фильтры'])

    keyboard_filters_years = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True)
    return keyboard_filters_years
