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
query_final_words = []
ids = []


def get_inline_keyboard_letters():
    start_index = (current_page - 1) * page_size

    inline_keyboard_letters = InlineKeyboardMarkup()

    for i in range(start_index, start_index + page_size):
        if i >= len(query_final_words):
            break
        inline_button = InlineKeyboardButton(query_final_words[i], callback_data=str(ids[i]))
        inline_keyboard_letters.add(inline_button)

    if len(inline_keyboard_letters.inline_keyboard) == 0:
        return None

    prev_button = InlineKeyboardButton("<- Назад", callback_data="prev")
    next_button = InlineKeyboardButton("Вперёд ->", callback_data="next")

    if current_page == 1:
        if len(inline_keyboard_letters.inline_keyboard) == 1:
            return inline_keyboard_letters
        inline_keyboard_letters.row(next_button)
    elif current_page > 1 and start_index + page_size >= len(query_final_words):
        inline_keyboard_letters.row(prev_button)
    else:
        inline_keyboard_letters.row(prev_button, next_button)

    return inline_keyboard_letters


def inline_keyboard_letters(choice):
    global current_page, query_final_words, ids
    current_page = 1
    query_final_words = []
    ids = []
    k = 1

    query_games_word = []
    for word in GamesData.select(GamesData.Name):
        query_games_word += [word.Name]

    query_games_word = sorted(query_games_word)

    for word in query_games_word:
        if word[0] == choice:
            query_final_words += [word]
            ids += [k]
        k += 1

    inline_keyboard_letters = get_inline_keyboard_letters()

    if len(query_final_words) <= page_size:
        inline_keyboard_letters.inline_keyboard = inline_keyboard_letters.inline_keyboard[:1]
        return inline_keyboard_letters

    return inline_keyboard_letters


@rate_limit(limit=3)
@dp.callback_query_handler(text="prev", state=SwitchMenu.Library_after_inline)
async def handle_prev_page(callback_query: types.CallbackQuery):
    global current_page, query_final_words, ids
    if current_page > 1:
        current_page -= 1

    inline_keyboard_letter = get_inline_keyboard_letters()

    try:
        if inline_keyboard_letter is not None:
            await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_letter)
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось


@rate_limit(limit=3)
@dp.callback_query_handler(text="next", state=SwitchMenu.Library_after_inline)
async def handle_next_page(callback_query: types.CallbackQuery):
    global current_page, query_final_words, ids
    current_page += 1

    inline_keyboard_letter = get_inline_keyboard_letters()

    try:
        if inline_keyboard_letter is not None:
            await callback_query.message.edit_reply_markup(reply_markup=inline_keyboard_letter)
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось
