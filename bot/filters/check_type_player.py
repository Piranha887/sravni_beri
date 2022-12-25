import re

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# ^([0-9]|([0-9][0-9]))[+]$

class PlayerCheck(BoundFilter):
    async def check(self, message: types.Message):
        try:
            pattern = re.compile(r"^\d{2}$|^\d{1,2}\-\d{1,3}$")
            return message.text == pattern.match(message.text).group(0)
        except:
            await message.answer("Нажмите на кнопку в меню")
            return False