from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from write_in_database import Buttons


def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def keyboard_filters_player():
    query_players = [player.player_buttons for player in Buttons.select()]

    lines_filters_player: List[List[Any]] = list(partition(query_players, 5))

    keyboard_buttons = []
    for line in lines_filters_player:
        keyboard_buttons.append(line)

    keyboard_buttons.append(['\U0001f519 Фильтры'])

    keyboard_filters_players = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True)
    return keyboard_filters_players
