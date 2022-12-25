from typing import List, Any

from aiogram.types import ReplyKeyboardMarkup
from peewee import *

from bot.data import config
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_library():
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)
    query_symbol = []
    for tag in Buttons.select():
        query_symbol += [tag.library_buttons]

    lines_library: List[Any] = list(partition(query_symbol, 5))

    keyboard_library = ReplyKeyboardMarkup(
        keyboard=[
            lines_library[0],
            lines_library[1],
            lines_library[2],
            lines_library[3],
            lines_library[4],
            lines_library[5],
            ['\U0001f519 Главное меню']
        ], resize_keyboard=True
    )
    return keyboard_library
