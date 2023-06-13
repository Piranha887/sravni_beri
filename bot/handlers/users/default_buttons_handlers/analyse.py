# Импорт необходимых модулей и классов
from bot.states import SwitchMenu  # Импорт класса SwitchMenu из модуля bot.states
from bot.loader import dp  # Импорт объекта dp из модуля bot.loader
from aiogram import types  # Импорт классов types из модуля aiogram
from bot.utils.misc import rate_limit  # Импорт функции rate_limit из модуля bot.utils.misc


# Декоратор для ограничения частоты вызова обработчика сообщений
@rate_limit(limit=3)
@dp.message_handler(text='Гистограмма "\U0001f465 Количество игроков"', state=SwitchMenu.Analyse)
async def show_hist_players(message: types.Message):
    # Отправка фотографии в ответ на сообщение
    await message.reply_photo(photo=open("../analyse/images/player.png", 'rb'))


# Декоратор для ограничения частоты вызова обработчика сообщений
@rate_limit(limit=3)
@dp.message_handler(text='Гистограмма "\U0001f522 Возраст"', state=SwitchMenu.Analyse)
async def show_hist_ages(message: types.Message):
    # Отправка фотографии в ответ на сообщение
    await message.reply_photo(photo=open("../analyse/images/age.png", 'rb'))


# Декоратор для ограничения частоты вызова обработчика сообщений
@rate_limit(limit=3)
@dp.message_handler(text='Гистограмма "\U0001f4c5 Год выпуска"', state=SwitchMenu.Analyse)
async def show_hist_years(message: types.Message):
    # Отправка фотографии в ответ на сообщение
    await message.reply_photo(photo=open("../analyse/images/year.png", 'rb'))


# Декоратор для ограничения частоты вызова обработчика сообщений
@rate_limit(limit=3)
@dp.message_handler(text='Гистограмма "\u2699 Издатель"', state=SwitchMenu.Analyse)
async def show_hist_manufactures(message: types.Message):
    # Отправка фотографии в ответ на сообщение
    await message.reply_photo(photo=open("../analyse/images/manufacture.png", 'rb'))
