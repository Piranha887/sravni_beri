from aiogram.dispatcher.filters.state import StatesGroup, State


class SwitchMenu(StatesGroup):
    Main = State()
    Library = State()
    Analyse = State()
    Filters = State()
    Filters_players = State()
    Filters_ages = State()
    Filters_manufactories = State()
    Filters_years = State()
    Show = State()

