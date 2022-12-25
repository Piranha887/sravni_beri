from aiogram import types
from aiogram.dispatcher.filters import Command

from bot.keyboards.default import keyboard_start, keyboard_library, keyboard_filters, keyboard_filters_player, \
    keyboard_filters_age, keyboard_filters_year, keyboard_filters_manufactory
from bot.keyboards.default.keyboard_analyse import keyboard_analyse
from bot.loader import dp
from bot.states import SwitchMenu
from bot.utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler(Command("menu"))
async def show_menu_start(message: types.Message):
    await message.answer("Нажмите кнопку из меню ниже", reply_markup=keyboard_start)
    await SwitchMenu.first()


@dp.message_handler(text="\U0001f4dc Описание", state=SwitchMenu.Main)
async def show_description(message: types.Message):
    await message.reply('"Сравни, Бери!" - бот Telegram, который показывает ' +
                        "информацию об одинаковых" +
                        " настольных играх на разных " +
                        "торговых онлайн площадках")


@dp.message_handler(text="\U0001f4de Контакты", state=SwitchMenu.Main)
async def show_contacts(message: types.Message):
    await message.reply('По вопросам и предложениям пишите: @piranha887')


@dp.message_handler(text="\U0001f4d6 Библиотека", state=SwitchMenu.Main)
async def show_menu_library(message: types.Message):
    await message.answer("Выберите букву, на которую начинается название игры:", reply_markup=keyboard_library())
    await SwitchMenu.Library.set()

    @dp.message_handler(text="\U0001f519 Главное меню", state=SwitchMenu.Library)
    async def show_back(message: types.Message):
        await message.reply("Главное меню", reply_markup=keyboard_start)
        await SwitchMenu.Main.set()


@dp.message_handler(text="\U0001f50e Анализ", state=SwitchMenu.Main)
async def show_menu_analyse(message: types.Message):
    await message.answer("Выберите одну из гистрограмм в меню ниже:", reply_markup=keyboard_analyse())
    await SwitchMenu.Analyse.set()

    @dp.message_handler(text="\U0001f519 Главное меню", state=SwitchMenu.Analyse)
    async def show_back(message: types.Message):
        await message.reply("Главное меню", reply_markup=keyboard_start)
        await SwitchMenu.Main.set()


@dp.message_handler(text="\U0001f9ee Фильтры", state=SwitchMenu.Main)
async def show_menu_filters(message: types.Message):
    await message.answer("Выберите один из фильтров:", reply_markup=keyboard_filters())
    await SwitchMenu.Filters.set()

    @dp.message_handler(text="\U0001f522 Возраст", state=SwitchMenu.Filters)
    async def show_menu_filters_ages(message: types.Message):
        await message.answer("Выберите один из возрастов:", reply_markup=keyboard_filters_age())
        await SwitchMenu.Filters_ages.set()

        @dp.message_handler(text="\U0001f519 Фильтры", state=SwitchMenu.Filters_ages)
        async def show_back(message: types.Message):
            await message.reply("Фильтры", reply_markup=keyboard_filters())
            await SwitchMenu.Filters.set()

    @dp.message_handler(text="\U0001f465 Количество игроков", state=SwitchMenu.Filters)
    async def show_menu_filters_players(message: types.Message):
        await message.answer("Выберите одну из категорий:", reply_markup=keyboard_filters_player())
        await SwitchMenu.Filters_players.set()

        @dp.message_handler(text="\U0001f519 Фильтры", state=SwitchMenu.Filters_players)
        async def show_back(message: types.Message):
            await message.reply("Фильтры", reply_markup=keyboard_filters())
            await SwitchMenu.Filters.set()

    @dp.message_handler(text="\U0001f4c5 Год выпуска", state=SwitchMenu.Filters)
    async def show_menu_filters_years(message: types.Message):
        await message.answer("Выберите один из годов:", reply_markup=keyboard_filters_year())
        await SwitchMenu.Filters_years.set()

        @dp.message_handler(text="\U0001f519 Фильтры", state=SwitchMenu.Filters_years)
        async def show_back(message: types.Message):
            await message.reply("Фильтры", reply_markup=keyboard_filters())
            await SwitchMenu.Filters.set()

    @dp.message_handler(text="\u2699 Издатель", state=SwitchMenu.Filters)
    async def show_menu_filters_manufactories(message: types.Message):
        await message.answer("Выберите производителя:", reply_markup=keyboard_filters_manufactory())
        await SwitchMenu.Filters_manufactories.set()

        @dp.message_handler(text="\U0001f519 Фильтры", state=SwitchMenu.Filters_manufactories)
        async def show_back(message: types.Message):
            await message.reply("Фильтры", reply_markup=keyboard_filters())
            await SwitchMenu.Filters.set()

    @dp.message_handler(text="\U0001f519 Главное меню", state=SwitchMenu.Filters)
    async def show_back(message: types.Message):
        await message.reply("Главное меню", reply_markup=keyboard_start)
        await SwitchMenu.Main.set()
