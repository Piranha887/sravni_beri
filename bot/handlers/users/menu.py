# Импорт необходимых модулей и классов
from aiogram import types  # Импорт типов и классов aiogram
from aiogram.dispatcher.filters import Command  # Импорт фильтра для команды
from bot.keyboards.default import (
    keyboard_start, keyboard_library, keyboard_filters, keyboard_filters_player,
    keyboard_filters_age, keyboard_filters_year, keyboard_filters_manufactory,
    keyboard_analyse)  # Импорт клавиатур
from bot.loader import dp  # Импорт экземпляра диспетчера
from bot.states import SwitchMenu  # Импорт состояния
from bot.utils.misc import rate_limit  # Импорт декоратора для ограничения частоты запросов


# Обработчик команды /menu
@rate_limit(limit=10)  # Ограничение частоты выполнения команды
@dp.message_handler(Command("menu"), state=[SwitchMenu.Main,
                                            SwitchMenu.Library, SwitchMenu.Analyse, SwitchMenu.Filters,
                                            SwitchMenu.Filters_ages, SwitchMenu.Filters_players,
                                            SwitchMenu.Filters_manufactories, SwitchMenu.Filters_years,
                                            SwitchMenu.Library_after_inline, SwitchMenu.Filters_ages_after_inline,
                                            SwitchMenu.Filters_players_after_inline,
                                            SwitchMenu.Filters_manufactories_after_inline,
                                            SwitchMenu.Filters_years_after_inline, SwitchMenu.Library_shows,
                                            SwitchMenu.Filters_ages_shows, SwitchMenu.Filters_players_shows,
                                            SwitchMenu.Filters_manufactories_shows, SwitchMenu.Filters_years_shows
                                            ])  # Обработка команды /menu
async def show_menu_start(message: types.Message):  # Функция-обработчик команды /menu
    await message.answer("Нажмите кнопку из меню ниже", reply_markup=keyboard_start)  # Ответ пользователю с клавиатурой
    await SwitchMenu.Main.set()  # Переход к состоянию SwitchMenu.Main


# Обработчики текстовых сообщений
@rate_limit(limit=3)
@dp.message_handler(text="\U0001f4dc Описание", state=SwitchMenu.Main)
async def show_description(message: types.Message):
    await message.reply(
        '"Сравни, Бери!" - бот Telegram, который показывает информацию об одинаковых настольных играх на разных торговых онлайн площадках')


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f4de Контакты", state=SwitchMenu.Main)
async def show_contacts(message: types.Message):
    await message.reply('По вопросам и предложениям пишите: @piranha887')


# Обработчики текстовых сообщений с определенным текстом
@rate_limit(limit=3)
@dp.message_handler(text="\U0001f4d6 Библиотека", state=SwitchMenu.Main)
async def show_menu_library(message: types.Message):
    await message.answer("Выберите букву, на которую начинается название игры:", reply_markup=keyboard_library())
    await SwitchMenu.Library.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f50e Анализ", state=SwitchMenu.Main)
async def show_menu_analyse(message: types.Message):
    await message.answer("Выберите одну из гистрограмм в меню ниже:", reply_markup=keyboard_analyse())
    await SwitchMenu.Analyse.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f9ee Фильтры", state=SwitchMenu.Main)
async def show_menu_filters(message: types.Message):
    await message.answer("Выберите один из фильтров:", reply_markup=keyboard_filters())
    await SwitchMenu.Filters.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f522 Возраст", state=SwitchMenu.Filters)
async def show_menu_filters_ages(message: types.Message):
    await message.answer("Выберите один из возрастов:", reply_markup=keyboard_filters_age())
    await SwitchMenu.Filters_ages.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f465 Количество игроков", state=SwitchMenu.Filters)
async def show_menu_filters_players(message: types.Message):
    await message.answer("Выберите одну из категорий:", reply_markup=keyboard_filters_player())
    await SwitchMenu.Filters_players.set()


@rate_limit(limit=3)
@dp.message_handler(text="\u2699 Издатель", state=SwitchMenu.Filters)
async def show_menu_filters_manufactories(message: types.Message):
    await message.answer("Выберите производителя:", reply_markup=keyboard_filters_manufactory())
    await SwitchMenu.Filters_manufactories.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f4c5 Год выпуска", state=SwitchMenu.Filters)
async def show_menu_filters_years(message: types.Message):
    await message.answer("Выберите один из годов:", reply_markup=keyboard_filters_year())
    await SwitchMenu.Filters_years.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f519 Главное меню", state=[
    SwitchMenu.Library, SwitchMenu.Analyse, SwitchMenu.Filters,
    SwitchMenu.Filters_ages, SwitchMenu.Filters_players,
    SwitchMenu.Filters_manufactories, SwitchMenu.Filters_years,
    SwitchMenu.Library_after_inline, SwitchMenu.Filters_ages_after_inline,
    SwitchMenu.Filters_players_after_inline, SwitchMenu.Filters_manufactories_after_inline,
    SwitchMenu.Filters_years_after_inline, SwitchMenu.Library_shows,
    SwitchMenu.Filters_ages_shows, SwitchMenu.Filters_players_shows,
    SwitchMenu.Filters_manufactories_shows, SwitchMenu.Filters_years_shows
])
async def show_back_to_main_menu(message: types.Message):
    await message.reply("Главное меню", reply_markup=keyboard_start)
    await SwitchMenu.Main.set()


@rate_limit(limit=3)
@dp.message_handler(text="\U0001f519 Фильтры", state=[
    SwitchMenu.Filters_ages, SwitchMenu.Filters_players,
    SwitchMenu.Filters_manufactories, SwitchMenu.Filters_years,
    SwitchMenu.Filters_ages_after_inline,
    SwitchMenu.Filters_players_after_inline,
    SwitchMenu.Filters_manufactories_after_inline,
    SwitchMenu.Filters_years_after_inline,
    SwitchMenu.Filters_ages_shows, SwitchMenu.Filters_players_shows,
    SwitchMenu.Filters_manufactories_shows, SwitchMenu.Filters_years_shows
])
async def show_back_to_filters_menu(message: types.Message):
    await message.reply("Фильтры", reply_markup=keyboard_filters())
    await SwitchMenu.Filters.set()
