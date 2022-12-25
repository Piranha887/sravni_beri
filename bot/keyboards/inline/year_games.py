from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_inline_paginations.paginator import Paginator
from bot.data import config
from peewee import *

from write_in_database import GamesData

from bot.loader import dp


async def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def inline_keyboard_filters_years(choice):
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)

    query_games_years = []
    # inline_buttons = []
    for year in GamesData.select().where(GamesData.Year == choice):
        query_games_years += [year.Name]

    # lines_filters_age: List[Any] = list(partition(query_games_ages, 4))
    inline_keyboard_filters_year = InlineKeyboardMarkup()
    for i in range(0, len(query_games_years)):
        inline_button = InlineKeyboardButton(query_games_years[i], callback_data=query_games_years[i])
        inline_keyboard_filters_year.add(inline_button)

    paginator = Paginator(data=inline_keyboard_filters_year, size=5, dp=dp)
    return paginator()
