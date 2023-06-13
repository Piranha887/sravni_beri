# Импорт необходимых модулей и классов
from aiogram import types  # Импорт классов types из модуля aiogram
from aiogram.dispatcher import FSMContext  # Импорт класса FSMContext из модуля aiogram.dispatcher
from aiogram.types import CallbackQuery  # Импорт класса CallbackQuery из модуля aiogram.types

from bot.filters.check_type_nogoback import \
    NoGoBackCheck  # Импорт класса NoGoBackCheck из модуля bot.filters.check_type_nogoback
from bot.filters.check_type_player import \
    PlayerCheck  # Импорт класса PlayerCheck из модуля bot.filters.check_type_player
from bot.handlers.users.auxiliary_functions.game_selection import \
    process_game_selection  # Импорт функции process_game_selection из модуля bot.handlers.users.auxiliary_functions.game_selection
from bot.shows.show_information import \
    show_game_information  # Импорт функции show_game_information из модуля bot.shows.show_information
from bot.keyboards.default import \
    keyboard_filter_main_menu  # Импорт функции keyboard_filter_main_menu из модуля bot.keyboards.default
from bot.keyboards.inline.player_games import \
    inline_keyboard_filters_players  # Импорт функции inline_keyboard_filters_players из модуля bot.keyboards.inline.player_games
from bot.loader import dp, bot  # Импорт объектов dp, bot из модуля bot.loader
from bot.states import SwitchMenu  # Импорт класса SwitchMenu из модуля bot.states
from bot.utils.misc import rate_limit  # Импорт функции rate_limit из модуля bot.utils.misc
from write_in_database import GamesData  # Импорт класса GamesData из модуля write_in_database


# Декоратор для ограничения частоты вызова обработчика сообщений
@rate_limit(limit=3)
@dp.message_handler(PlayerCheck(), state=SwitchMenu.Filters_players)
async def show_player_games(message: types.Message, state: FSMContext):
    # Отправка ответного сообщения с выбранным игроком
    await message.answer("Ваш выбор игрока: " + message.text)
    # Отправка сообщения с выбором игры и кнопками для игрока
    msg = await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_players(message.text))
    # Отправка сообщения с инструкцией пользователю и кнопками "Фильтры" и "Главное меню"
    await message.answer(
        'Вы можете вернуться обратно с помощью команд "\U0001f519 Фильтры" и "\U0001f519 Главное меню"',
        reply_markup=keyboard_filter_main_menu())
    # Получение списка игр, связанных с выбранным игроком
    query_games_players = []
    for player in GamesData.select().where(GamesData.Player == message.text):
        query_games_players += [player.Name]
    await state.update_data(msg_id=msg.message_id)  # Сохранение ID сообщения в состоянии
    await SwitchMenu.Filters_players_after_inline.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(NoGoBackCheck(), state=SwitchMenu.Filters_players_after_inline)
async def player_answer(call: CallbackQuery, state: FSMContext):
    # Обработка выбранной игры игрока
    await process_game_selection(call, state, bot)
    await SwitchMenu.Filters_players_shows.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text='Сообщение', state=SwitchMenu.Filters_players_shows)
async def show_game_msg(call: CallbackQuery, state: FSMContext):
    # Отображение информации об игре типа "Сообщение"
    await show_game_information(call, state, "Сообщение")
    await SwitchMenu.Filters_players.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text='PDF', state=SwitchMenu.Filters_players_shows)
async def show_game_pdf(call: CallbackQuery, state: FSMContext):
    # Отображение информации об игре типа "PDF"
    await show_game_information(call, state, "PDF")
    await SwitchMenu.Filters_players.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text='HTML', state=SwitchMenu.Filters_players_shows)
async def show_game_html(call: CallbackQuery, state: FSMContext):
    # Отображение информации об игре типа "HTML"
    await show_game_information(call, state, "HTML")
    await SwitchMenu.Filters_players.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text="Назад", state=SwitchMenu.Filters_players_shows)
async def show_back_to_players_menu(call: CallbackQuery, state: FSMContext):
    # Обработка callback-запроса для возврата к меню выбора игрока
    data = await state.get_data()
    msg_inline_msg_html_id = data.get('msg_inline_msg_html_id')
    await bot.delete_message(call.message.chat.id, msg_inline_msg_html_id)
    await SwitchMenu.Filters_players.set()
    await call.message.answer("Выберите букву из меню")  # Отправка сообщения с инструкцией пользователю
