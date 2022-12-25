import re

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AgeCheck(BoundFilter):
    async def check(self, message: types.Message):
        try:
            pattern = re.compile(r"^\d{1,2}[+]$")
            return message.text == pattern.match(message.text).group(0)
        except:
            await message.answer("Нажмите на кнопку в меню")
            return False

