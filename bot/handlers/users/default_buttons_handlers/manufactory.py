from aiogram import types
from aiogram.types import CallbackQuery

from bot.handlers.users.show_game import show_game
from bot.keyboards.inline.manufactory_games import inline_keyboard_filters_manufactories
from bot.loader import dp

from bot.states import SwitchMenu
from write_in_database import GamesData


@dp.message_handler(state=SwitchMenu.Filters_manufactories)
async def show_manufacture_games(message: types.Message):
    await message.answer("Ваш выбор производителя: " + message.text)

    await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_manufactories(message.text))

    query_games_manufactory = []
    # inline_buttons = []
    for manufactory in GamesData.select().where(GamesData.Manufacture == message.text):
        query_games_manufactory += [manufactory.Name]

    @dp.callback_query_handler(state=SwitchMenu.Filters_manufactories)
    async def manufactory_answer(call: CallbackQuery):
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