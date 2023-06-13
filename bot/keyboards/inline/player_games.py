from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from peewee import *
from bot.data import config
from bot.loader import dp
from bot.states import SwitchMenu
from bot.utils.misc import rate_limit
from write_in_database import GamesData
from aiogram.utils.exceptions import MessageNotModified

# global current_page
current_page = 1
page_size = 5
query_games_players = []
ids = []


def get_inline_keyboard_filters_players():
    start_index = (current_page - 1) * page_size

    inline_keyboard_filters_players = InlineKeyboardMarkup()

    for i in range(start_index, start_index + page_size):
        if i >= len(query_games_players):
            break
        inline_button = InlineKeyboardButton(query_games_players[i], callback_data=str(ids[i]))
        inline_keyboard_filters_players.add(inline_button)

    if len(inline_keyboard_filters_players.inline_keyboard) == 0:
        return None

    prev_button = InlineKeyboardButton("<- Назад", callback_data="prev")
    next_button = InlineKeyboardButton("Вперёд ->", callback_data="next")

    if current_page == 1:
        if len(inline_keyboard_filters_players.inline_keyboard) == 1:
            return inline_keyboard_filters_players
        inline_keyboard_filters_players.row(next_button)
    elif current_page > 1 and start_index + page_size >= len(query_games_players):
        inline_keyboard_filters_players.row(prev_button)
    else:
        inline_keyboard_filters_players.row(prev_button, next_button)

    return inline_keyboard_filters_players


def inline_keyboard_filters_players(choice):
    global current_page, query_games_players, ids
    current_page = 1
    query_games_players = []
    ids = []

    for player in GamesData.select().where(GamesData.Player == choice):
        query_games_players += [player.Name]
        ids += [player.id]

    inline_keyboard_filters_players = get_inline_keyboard_filters_players()

    if inline_keyboard_filters_players is not None:
        return inline_keyboard_filters_players
    else:
        current_page -= 1
        inline_keyboard_filters_players = get_inline_keyboard_filters_players()
        return inline_keyboard_filters_players


@rate_limit(limit=3)
@dp.callback_query_handler(text="prev", state=SwitchMenu.Filters_players_after_inline)
async def handle_prev_page(callback_query: types.CallbackQuery):
    global current_page, query_games_players, ids
    if current_page > 1:
        current_page -= 1

    inline_keyboard_filters_players = get_inline_keyboard_filters_players()

    try:
        if inline_keyboard_filters_players is not None:
            await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_filters_players)
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось


@rate_limit(limit=3)
@dp.callback_query_handler(text="next", state=SwitchMenu.Filters_players_after_inline)
async def handle_next_page(callback_query: types.CallbackQuery):
    global current_page, query_games_players, ids
    current_page += 1

    inline_keyboard_filters_players = get_inline_keyboard_filters_players()

    try:
        if inline_keyboard_filters_players is not None:
            await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_filters_players)
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось
