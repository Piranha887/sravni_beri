from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from bot.data import config
from peewee import *
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_manufactory():
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)
    query_manufactories = []
    for manufacture in Buttons.select():
        query_manufactories += [manufacture.manufacture_buttons]

    lines_filters_manufactory: List[Any] = list(partition(query_manufactories, 4))

    keyboard_filters_manufactory = ReplyKeyboardMarkup(
        keyboard=[
            lines_filters_manufactory[0],
            lines_filters_manufactory[1],
            lines_filters_manufactory[2],
            lines_filters_manufactory[3],
            lines_filters_manufactory[4],
            ['\U0001f519 Фильтры']
        ], resize_keyboard=True
    )
    return keyboard_filters_manufactory
