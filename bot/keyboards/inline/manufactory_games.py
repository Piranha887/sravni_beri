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
query_games_manufactory = []
ids = []


def get_inline_keyboard_filters_manufactory():
    start_index = (current_page - 1) * page_size

    inline_keyboard_filters_manufactory = InlineKeyboardMarkup()

    for i in range(start_index, start_index + page_size):
        if i >= len(query_games_manufactory):
            break
        inline_button = InlineKeyboardButton(query_games_manufactory[i], callback_data=str(ids[i]))
        inline_keyboard_filters_manufactory.add(inline_button)

    if len(inline_keyboard_filters_manufactory.inline_keyboard) == 0:
        return None

    prev_button = InlineKeyboardButton("<- Назад", callback_data="prev")
    next_button = InlineKeyboardButton("Вперёд ->", callback_data="next")

    if current_page == 1:
        if len(inline_keyboard_filters_manufactory.inline_keyboard) == 1:
            return inline_keyboard_filters_manufactory
        inline_keyboard_filters_manufactory.row(next_button)
    elif current_page > 1 and start_index + page_size >= len(query_games_manufactory):
        inline_keyboard_filters_manufactory.row(prev_button)
    else:
        inline_keyboard_filters_manufactory.row(prev_button, next_button)

    return inline_keyboard_filters_manufactory


def inline_keyboard_filters_manufactories(choice):
    global current_page, query_games_manufactory, ids
    current_page = 1
    query_games_manufactory = []
    ids = []

    for manufactory in GamesData.select().where(GamesData.Manufacture == choice):
        query_games_manufactory += [manufactory.Name]
        ids += [manufactory.id]

    inline_keyboard_filters_manufactory = get_inline_keyboard_filters_manufactory()

    if len(query_games_manufactory) <= page_size:
        inline_keyboard_filters_manufactory.inline_keyboard = inline_keyboard_filters_manufactory.inline_keyboard[:1]
        return inline_keyboard_filters_manufactory


    @rate_limit(limit=3)
    @dp.callback_query_handler(text="prev", state=SwitchMenu.Filters_manufactories_after_inline)
    async def handle_prev_page(callback_query: types.CallbackQuery):
        global current_page, query_games_manufactory, ids
        if current_page > 1:
            current_page -= 1

        inline_keyboard_filters_manufactory = get_inline_keyboard_filters_manufactory()

        try:
            if inline_keyboard_filters_manufactory is not None:
                await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_filters_manufactory)
        except MessageNotModified:
            pass  # Просто игнорируем ошибку, если сообщение не изменилось


    @rate_limit(limit=3)
    @dp.callback_query_handler(text="next", state=SwitchMenu.Filters_manufactories_after_inline)
    async def handle_next_page(callback_query: types.CallbackQuery):
        global current_page, query_games_manufactory, ids
        current_page += 1

        inline_keyboard_filters_manufactory = get_inline_keyboard_filters_manufactory()

        try:
            if inline_keyboard_filters_manufactory is not None:
                await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_filters_manufactory)
        except MessageNotModified:
            pass  # Просто игнорируем ошибку, если сообщение не изменилось


    return inline_keyboard_filters_manufactory
