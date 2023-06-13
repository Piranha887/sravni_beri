from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from bot.loader import dp
from bot.states import SwitchMenu

from bot.utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Запустить бота'
        '/menu - Главное меню',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))
    await SwitchMenu.first()
