from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_inline_paginations.paginator import Paginator
from peewee import *

from bot.data import config
from bot.loader import dp
from write_in_database import GamesData


def inline_keyboard_filters_letters(choice):
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)
    query_final_words = []

    query_games_word = []
    for word in GamesData.select(GamesData.Name):
        query_games_word += [word.Name]

    for word in query_games_word:
        if word[0] == choice:
            query_final_words += [word]

    inline_keyboard_filters_letter = InlineKeyboardMarkup()
    for i in range(0, len(query_final_words)):
        inline_button = InlineKeyboardButton(query_final_words[i], callback_data=query_final_words[i])
        inline_keyboard_filters_letter.add(inline_button)

    paginator = Paginator(data=inline_keyboard_filters_letter, size=5, dp=dp)
    return paginator()
