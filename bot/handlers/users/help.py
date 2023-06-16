from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from bot.loader import dp
from bot.states import SwitchMenu

from bot.utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler(CommandHelp(), state=[SwitchMenu.Main,
                                          SwitchMenu.Library, SwitchMenu.Analyse, SwitchMenu.Filters,
                                          SwitchMenu.Filters_ages, SwitchMenu.Filters_players,
                                          SwitchMenu.Filters_manufactories, SwitchMenu.Filters_years,
                                          SwitchMenu.Library_after_inline, SwitchMenu.Filters_ages_after_inline,
                                          SwitchMenu.Filters_players_after_inline,
                                          SwitchMenu.Filters_manufactories_after_inline,
                                          SwitchMenu.Filters_years_after_inline, SwitchMenu.Library_shows,
                                          SwitchMenu.Filters_ages_shows, SwitchMenu.Filters_players_shows,
                                          SwitchMenu.Filters_manufactories_shows, SwitchMenu.Filters_years_shows
                                          ])
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Запустить бота'
        '/menu - Главное меню',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))
    await SwitchMenu.first()
