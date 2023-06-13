from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.filters.check_type_nogoback import NoGoBackCheck
from bot.filters.check_type_year import YearCheck
from bot.handlers.users.auxiliary_functions.game_selection import process_game_selection
from bot.shows.show_information import show_game_information
from bot.keyboards.default import keyboard_filter_main_menu
from bot.keyboards.inline.year_games import inline_keyboard_filters_years
from bot.loader import dp, bot

from bot.states import SwitchMenu
from bot.utils.misc import rate_limit
from write_in_database import GamesData


@rate_limit(limit=3)
@dp.message_handler(YearCheck(), state=SwitchMenu.Filters_years)
async def show_year_games(message: types.Message, state: FSMContext):
    await message.answer("Ваш выбор возраста: " + message.text)

    msg = await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_years(message.text))
    await message.answer(
        'Вы можете вернуться обратно с помощью команд "\U0001f519 Фильтры" и "\U0001f519 Главное меню"',
        reply_markup=keyboard_filter_main_menu())
    query_games_years = []
    for year in GamesData.select().where(GamesData.Year == message.text):
        query_games_years += [year.Name]

    await state.update_data(msg_id=msg.message_id)  # Сохраняем ID сообщения в состоянии
    await SwitchMenu.Filters_years_after_inline.set()


@rate_limit(limit=3)
@dp.callback_query_handler(NoGoBackCheck(), state=SwitchMenu.Filters_years_after_inline)
async def year_answer(call: CallbackQuery, state: FSMContext):
    await process_game_selection(call, state, bot)
    await SwitchMenu.Filters_years_shows.set()


@rate_limit(limit=3)
@dp.callback_query_handler(text='Сообщение', state=SwitchMenu.Filters_years_shows)
async def show_game_msg(call: CallbackQuery, state: FSMContext):
    await show_game_information(call, state, "Сообщение")
    await SwitchMenu.Filters_years.set()


@rate_limit(limit=3)
@dp.callback_query_handler(text='PDF', state=SwitchMenu.Filters_years_shows)
async def show_game_pdf(call: CallbackQuery, state: FSMContext):
    await show_game_information(call, state, "PDF")
    await SwitchMenu.Filters_years.set()


@rate_limit(limit=3)
@dp.callback_query_handler(text='HTML', state=SwitchMenu.Filters_years_shows)
async def show_game_html(call: CallbackQuery, state: FSMContext):
    await show_game_information(call, state, "HTML")
    await SwitchMenu.Filters_years.set()


@rate_limit(limit=3)
@dp.callback_query_handler(text="Назад", state=SwitchMenu.Filters_years_shows)
async def show_back_to_years_menu(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_inline_msg_html_id = data.get('msg_inline_msg_html_id')
    await bot.delete_message(call.message.chat.id, msg_inline_msg_html_id)
    await SwitchMenu.Filters_years.set()
    await call.message.answer("Выберите кнопку из меню")  # Отправляем сообщение с инструкцией пользователю
