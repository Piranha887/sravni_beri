from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from bot.data import config
from peewee import *
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_age():
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)
    query_ages = []
    for age in Buttons.select():
        query_ages += [age.age_buttons]

    lines_filters_age: List[Any] = list(partition(query_ages, 4))

    keyboard_filters_age = ReplyKeyboardMarkup(
        keyboard=[
            lines_filters_age[0],
            lines_filters_age[1],
            lines_filters_age[2],
            ['\U0001f519 Фильтры']
        ], resize_keyboard=True
    )
    return keyboard_filters_age
