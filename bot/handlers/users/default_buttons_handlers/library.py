from aiogram import types
from aiogram.types import CallbackQuery

from bot.handlers.users.show_game import show_game
from bot.keyboards.inline.letter_games import inline_keyboard_filters_letters
from bot.loader import dp
from bot.keyboards.default import keyboard_library
from bot.filters.check_type_letter import LetterTypeCheck
from bot.states import SwitchMenu
from write_in_database import GamesData


@dp.message_handler(LetterTypeCheck(), state=SwitchMenu.Library)
async def show_letter_games(message: types.Message):
    await message.answer("Ваша буква: " + message.text)

    await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_letters(message.text))


    @dp.callback_query_handler(state=SwitchMenu.Library)
    async def letter_answer(call: CallbackQuery):
        await call.answer(cache_time=60)
        for game in GamesData.select().where(GamesData.Name == call.data):
            await call.answer(cache_time=60)
            media = types.MediaGroup()
            try:
                media.attach_photo(game.Image_HG)
            except:
                pass
            try:
                media.attach_photo(game.Image_GA)
            except:
                pass
            try:
                media.attach_photo(game.Image_LI)
            except:
                pass

            await call.message.answer(
                show_game(game))

            await call.message.answer_media_group(media=media)
