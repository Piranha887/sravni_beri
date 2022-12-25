from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from bot.data import config
from peewee import *
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_year():
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)
    query_years = []
    for year in Buttons.select():
        query_years += [year.year_buttons]

    lines_filters_year: List[Any] = list(partition(query_years, 3))

    keyboard_filters_year = ReplyKeyboardMarkup(
        keyboard=[
            lines_filters_year[0],
            lines_filters_year[1],
            lines_filters_year[2],
            lines_filters_year[3],
            lines_filters_year[4],
            ['\U0001f519 Фильтры']
        ], resize_keyboard=True
    )
    return keyboard_filters_year
