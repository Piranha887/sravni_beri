from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from bot.filters.check_type_age import AgeCheck
from bot.handlers.users.show_game import show_game
from bot.keyboards.inline.age_games import inline_keyboard_filters_age
from bot.loader import dp
from bot.states import SwitchMenu
from write_in_database import GamesData


@dp.message_handler(AgeCheck(), state=SwitchMenu.Filters_ages)
async def show_age_games(message: types.Message):
    await message.answer("Ваш выбор возраста: " + message.text)
    await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_age(message.text))
    query_games_ages = []
    for age in GamesData.select().where(GamesData.Age == message.text):
        query_games_ages += [age.Name]

    @dp.callback_query_handler(state=SwitchMenu.Filters_ages)
    async def age_answer(call: CallbackQuery):
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
            await call.message.answer(show_game(game))
            await call.message.answer_media_group(media=media)

