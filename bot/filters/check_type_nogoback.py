from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class NoGoBackCheck(BoundFilter):
    async def check(self, call: CallbackQuery):
        try:
            if "next" in call.data or "prev" in call.data:
                return False
            return True
        except:
            return False
