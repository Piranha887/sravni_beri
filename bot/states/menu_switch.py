from aiogram.dispatcher.filters.state import StatesGroup, State


# Определяем класс, представляющий различные состояния меню
class SwitchMenu(StatesGroup):
    # Reboot = State()
    Main = State()  # Состояние, представляющее главное меню
    Library = State()  # Состояние, представляющее меню библиотеки
    Library_after_inline = State()  # Состояние, представляющее меню библиотеки после инлайн-запроса
    Library_shows = State()  # Состояние, представляющее меню показов в библиотеке
    Analyse = State()  # Состояние, представляющее меню анализа
    Filters = State()  # Состояние, представляющее меню фильтров
    Filters_players = State()  # Состояние, представляющее меню фильтров по игрокам
    Filters_players_after_inline = State()  # Состояние, представляющее меню фильтров по игрокам после инлайн-запроса
    Filters_players_shows = State()  # Состояние, представляющее меню показов по игрокам
    Filters_ages = State()  # Состояние, представляющее меню фильтров по возрастам
    Filters_ages_after_inline = State()  # Состояние, представляющее меню фильтров по возрастам после инлайн-запроса
    Filters_ages_shows = State()  # Состояние, представляющее меню показов по возрастам
    Filters_years = State()  # Состояние, представляющее меню фильтров по годам
    Filters_years_after_inline = State()  # Состояние, представляющее меню фильтров по годам после инлайн-запроса
    Filters_years_shows = State()  # Состояние, представляющее меню показов по годам
    Filters_manufactories = State()  # Состояние, представляющее меню фильтров по производителям
    Filters_manufactories_after_inline = State()  # Состояние, представляющее меню фильтров по производителям после инлайн-запроса
    Filters_manufactories_shows = State()  # Состояние, представляющее меню показов по производителям
