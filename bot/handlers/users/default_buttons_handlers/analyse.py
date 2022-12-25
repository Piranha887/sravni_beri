from bot.states import SwitchMenu
from bot.loader import dp
from aiogram import types


@dp.message_handler(text='Гистограмма "\U0001f465 Количество игроков"', state=SwitchMenu.Analyse)
async def show_hist_players(message: types.Message):
    await message.reply_photo(photo=open("../analyse/images/player.png", 'rb'))


@dp.message_handler(text='Гистограмма "\U0001f522 Возраст"', state=SwitchMenu.Analyse)
async def show_hist_ages(message: types.Message):
    await message.reply_photo(photo=open("../analyse/images/age.png", 'rb'))


@dp.message_handler(text='Гистограмма "\U0001f4c5 Год выпуска"', state=SwitchMenu.Analyse)
async def show_hist_years(message: types.Message):
    await message.reply_photo(photo=open("../analyse/images/year.png", 'rb'))


@dp.message_handler(text='Гистограмма "\u2699 Издатель"', state=SwitchMenu.Analyse)
async def show_hist_manufactures(message: types.Message):
    await message.reply_photo(photo=open("../analyse/images/manufacture.png", 'rb'))
