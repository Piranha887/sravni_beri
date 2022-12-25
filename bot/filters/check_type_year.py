import re

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# ^([0-9]|([0-9][0-9]))[+]$

class YearCheck(BoundFilter):
    async def check(self, message: types.Message):
        try:
            pattern = re.compile(r"^(19|20)\d{2}$")
            return message.text == pattern.match(message.text).group(0)
        except:
            await message.answer("Нажмите на кнопку в меню")
            return False
