from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from bot.loader import dp
from bot.states import SwitchMenu
from bot.utils.misc import rate_limit
from write_in_database import GamesData
from aiogram.utils.exceptions import MessageNotModified

current_page = 1
page_size = 5
query_games_years = []
ids = []

def get_inline_keyboard_filters_years():
    start_index = (current_page - 1) * page_size

    inline_keyboard_filters_years = InlineKeyboardMarkup()

    for i in range(start_index, start_index + page_size):
        if i >= len(query_games_years):
            break
        inline_button = InlineKeyboardButton(query_games_years[i], callback_data=str(ids[i]))
        inline_keyboard_filters_years.add(inline_button)

    if len(inline_keyboard_filters_years.inline_keyboard) == 0:
        return None

    prev_button = InlineKeyboardButton("<- Назад", callback_data="prev")
    next_button = InlineKeyboardButton("Вперёд ->", callback_data="next")

    if current_page == 1:
        if len(inline_keyboard_filters_years.inline_keyboard) == 1:
            return inline_keyboard_filters_years
        inline_keyboard_filters_years.row(next_button)
    elif current_page > 1 and start_index + page_size >= len(query_games_years):
        inline_keyboard_filters_years.row(prev_button)
    else:
        inline_keyboard_filters_years.row(prev_button, next_button)

    return inline_keyboard_filters_years


def inline_keyboard_filters_years(choice):
    global current_page, query_games_years, ids
    current_page = 1
    query_games_years = []
    ids = []

    for year in GamesData.select().where(GamesData.Year == choice):
        query_games_years += [year.Name]
        ids += [year.id]

    inline_keyboard_filters_years = get_inline_keyboard_filters_years()

    if inline_keyboard_filters_years is not None:
        return inline_keyboard_filters_years

    current_page -= 1
    inline_keyboard_filters_years = get_inline_keyboard_filters_years()
    return inline_keyboard_filters_years


@rate_limit(limit=3)
@dp.callback_query_handler(text="prev", state=SwitchMenu.Filters_years_after_inline)
async def handle_prev_page(callback_query: types.CallbackQuery):
    global current_page, query_games_years, ids
    if current_page > 1:
        current_page -= 1

    inline_keyboard_filters_years = get_inline_keyboard_filters_years()

    try:
        if inline_keyboard_filters_years is not None:
            await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_filters_years)
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось


@rate_limit(limit=3)
@dp.callback_query_handler(text="next", state=SwitchMenu.Filters_years_after_inline)
async def handle_next_page(callback_query: types.CallbackQuery):
    global current_page, query_games_years, ids
    current_page += 1

    inline_keyboard_filters_years = get_inline_keyboard_filters_years()

    try:
        if inline_keyboard_filters_years is not None:
            await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_filters_years)
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось
