from aiogram import types
from aiogram.types import CallbackQuery

from bot.filters.check_type_player import PlayerCheck
from bot.handlers.users.show_game import show_game
from bot.keyboards.inline.player_games import inline_keyboard_filters_players
from bot.loader import dp
from bot.keyboards.default import keyboard_library
from bot.filters.check_type_letter import LetterTypeCheck
from bot.states import SwitchMenu
from write_in_database import GamesData


@dp.message_handler(PlayerCheck(), state=SwitchMenu.Filters_players)
async def show_player_games(message: types.Message):
    await message.answer("Ваш выбор игрока: " + message.text)

    await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_filters_players(message.text))

    query_games_players = []
    for player in GamesData.select().where(GamesData.Player == message.text):
        query_games_players += [player.Name]

    @dp.callback_query_handler(state=SwitchMenu.Filters_players)
    async def player_answer(call: CallbackQuery):
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

