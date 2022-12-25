from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_inline_paginations.paginator import Paginator
from peewee import *

from bot.data import config
from bot.loader import dp
from write_in_database import GamesData


def inline_keyboard_filters_age(choice):
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)

    query_games_ages = []

    for age in GamesData.select().where(GamesData.Age == choice):
        query_games_ages += [age.Name]

    inline_keyboard_filters_age = InlineKeyboardMarkup()
    for i in range(0, len(query_games_ages)):
        inline_button = InlineKeyboardButton(query_games_ages[i], callback_data=query_games_ages[i])
        inline_keyboard_filters_age.add(inline_button)

    paginator = Paginator(data=inline_keyboard_filters_age, size=5, dp=dp)
    return paginator()

