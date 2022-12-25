from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from bot.data import config
from peewee import *
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_player():
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)
    query_players = []
    for player in Buttons.select():
        query_players += [player.player_buttons]

    lines_filters_player: List[Any] = list(partition(query_players, 6))

    keyboard_filters_player = ReplyKeyboardMarkup(
        keyboard=[
            lines_filters_player[0],
            lines_filters_player[1],
            lines_filters_player[2],
            lines_filters_player[3],
            lines_filters_player[4],
            ['\U0001f519 Фильтры']
        ], resize_keyboard=True
    )
    return keyboard_filters_player
