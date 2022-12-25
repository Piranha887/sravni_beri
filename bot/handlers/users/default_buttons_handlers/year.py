from aiogram import types
from aiogram.types import CallbackQuery

from bot.filters.check_type_year import YearCheck
from bot.handlers.users.show_game import show_game
from bot.keyboards.inline.year_games import inline_keyboard_filters_years
from bot.loader import dp

from bot.states import SwitchMenu
from write_in_database import GamesData


@dp.message_handler(YearCheck(), state=SwitchMenu.Filters_years)
async def show_year_games(message: types.Message):
    await message.answer("Ваш выбор года: " + message.text)

    await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_years(message.text))

    query_games_years = []
    for player in GamesData.select().where(GamesData.Player == message.text):
        query_games_years += [player.Name]

    @dp.callback_query_handler(state=SwitchMenu.Filters_years)
    async def year_answer(call: CallbackQuery):
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