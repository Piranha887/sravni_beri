from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_inline_paginations.paginator import Paginator
from bot.data import config
from peewee import *

from write_in_database import GamesData

from bot.loader import dp


async def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def inline_keyboard_filters_manufactories(choice):
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)

    query_games_manufactory = []
    # inline_buttons = []
    for manufactory in GamesData.select().where(GamesData.Manufacture == choice):
        query_games_manufactory += [manufactory.Name]

    # lines_filters_age: List[Any] = list(partition(query_games_ages, 4))
    inline_keyboard_filters_manufactory = InlineKeyboardMarkup()
    for i in range(0, len(query_games_manufactory)):
        inline_button = InlineKeyboardButton(query_games_manufactory[i], callback_data=query_games_manufactory[i])
        inline_keyboard_filters_manufactory.add(inline_button)

    paginator = Paginator(data=inline_keyboard_filters_manufactory, size=5, dp=dp)
    return paginator()