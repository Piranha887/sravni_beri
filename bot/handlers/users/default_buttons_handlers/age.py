from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from bot.filters.check_type_age import AgeCheck
from bot.filters.check_type_nogoback import NoGoBackCheck
from bot.handlers.users.auxiliary_functions.game_selection import process_game_selection
from bot.shows.show_information import show_game_information
from bot.keyboards.default import keyboard_filter_main_menu
from bot.keyboards.inline.age_games import inline_keyboard_filters_age
from bot.loader import dp, bot
from bot.states import SwitchMenu
from write_in_database import GamesData


@dp.message_handler(AgeCheck(), state=SwitchMenu.Filters_ages)
async def show_age_games(message: types.Message, state: FSMContext):
    await message.answer("Ваш выбор возраста: " + message.text)
    msg = await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_age(message.text))
    await message.answer(
        'Вы можете вернуться обратно с помощью команд "\U0001f519 Фильтры" и "\U0001f519 Главное меню"',
        reply_markup=keyboard_filter_main_menu())
    # Получаем список игр, соответствующих выбранному возрасту из базы данных
    query_games_ages = []
    for age in GamesData.select().where(GamesData.Age == message.text):
        query_games_ages += [age.Name]

    await state.update_data(msg_id=msg.message_id)  # Сохраняем ID сообщения в состоянии
    await SwitchMenu.Filters_ages_after_inline.set()


@dp.callback_query_handler(NoGoBackCheck(), state=SwitchMenu.Filters_ages_after_inline)
async def age_answer(call: CallbackQuery, state: FSMContext):
    await process_game_selection(call, state, bot)
    await SwitchMenu.Filters_ages_shows.set()


@dp.callback_query_handler(text='Сообщение', state=SwitchMenu.Filters_ages_shows)
async def show_game_msg(call: CallbackQuery, state: FSMContext):
    await show_game_information(call, state, "Сообщение")
    await SwitchMenu.Filters_ages.set()


@dp.callback_query_handler(text='PDF', state=SwitchMenu.Filters_ages_shows)
async def show_game_pdf(call: CallbackQuery, state: FSMContext):
    await show_game_information(call, state, "PDF")
    await SwitchMenu.Filters_ages.set()


@dp.callback_query_handler(text='HTML', state=SwitchMenu.Filters_ages_shows)
async def show_game_html(call: CallbackQuery, state: FSMContext):
    await show_game_information(call, state, "HTML")
    await SwitchMenu.Filters_ages.set()


@dp.callback_query_handler(text="Назад", state=SwitchMenu.Filters_ages_shows)
async def show_back_to_ages_menu(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_inline_msg_html_id = data.get('msg_inline_msg_html_id')
    await bot.delete_message(call.message.chat.id, msg_inline_msg_html_id)
    await SwitchMenu.Filters_ages.set()
    await call.message.answer("Выберите возраст из меню")  # Отправляем сообщение с инструкцией пользователю
