from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.keyboards.default import keyboard_start
from bot.loader import dp
from bot.states import SwitchMenu
from bot.utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer("Нажмите кнопку из меню ниже", reply_markup=keyboard_start)
    await SwitchMenu.first()
