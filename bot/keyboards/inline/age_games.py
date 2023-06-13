# Импорт необходимых модулей и классов
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton  # Импорт классов для создания встроенной клавиатуры
from aiogram import types  # Импорт типов данных для работы с Telegram API
from bot.loader import dp  # Импорт диспетчера бота
from bot.states import SwitchMenu  # Импорт состояний бота
from bot.utils.misc import rate_limit  # Импорт декоратора для ограничения количества вызовов функции
from write_in_database import GamesData  # Импорт класса для работы с базой данных
from aiogram.utils.exceptions import MessageNotModified  # Импорт исключения для обработки неизмененного сообщения

# Глобальные переменные
current_page = 1  # Текущая страница
page_size = 5  # Размер страницы
query_games_ages = []  # Список запросов по возрасту
ids = []  # Список идентификаторов


# Функция для получения inline клавиатуры фильтров по возрасту
def get_inline_keyboard_filters_age():
    start_index = (current_page - 1) * page_size  # Вычисление индекса начального элемента на текущей странице

    inline_keyboard_filters_ages = InlineKeyboardMarkup()  # Создание объекта встроенной клавиатуры

    # Создание кнопок для каждого элемента в списке запросов
    for i in range(start_index, start_index + page_size):
        if i >= len(query_games_ages):
            break
        inline_button = InlineKeyboardButton(query_games_ages[i], callback_data=str(
            ids[i]))  # Создание кнопки с текстом из списка запросов и идентификатором
        inline_keyboard_filters_ages.add(inline_button)  # Добавление кнопки к встроенной клавиатуре

    # Проверка, если встроенной клавиатуры нет элементов, возвращаем None
    if len(inline_keyboard_filters_ages.inline_keyboard) == 0:
        return None

    prev_button = InlineKeyboardButton("<- Назад", callback_data="prev")  # Создание кнопки "Назад"
    next_button = InlineKeyboardButton("Вперёд ->", callback_data="next")  # Создание кнопки "Вперёд"

    # Добавление кнопок в зависимости от текущей страницы и количества элементов
    if current_page == 1:
        if len(inline_keyboard_filters_ages.inline_keyboard) == 1:
            return inline_keyboard_filters_ages
        inline_keyboard_filters_ages.row(next_button)  # Добавление кнопки "Вперёд" в отдельную строку
    elif current_page > 1 and start_index + page_size >= len(query_games_ages):
        inline_keyboard_filters_ages.row(prev_button)  # Добавление кнопки "Назад" в отдельную строку
    else:
        inline_keyboard_filters_ages.row(prev_button, next_button)  # Добавление кнопок "Назад" и "Вперёд" в одну строку

    return inline_keyboard_filters_ages  # Возвращаем встроенную клавиатуру


# Функция для обработки выбора возраста в inline клавиатуре фильтров
def inline_keyboard_filters_age(choice):
    global current_page, query_games_ages, ids  # Использование глобальных переменных
    current_page = 1  # Установка текущей страницы в начальное значение
    query_games_ages = []  # Очистка списка запросов по возрасту
    ids = []  # Очистка списка идентификаторов

    # Получение запросов и идентификаторов для выбранного возраста
    for age in GamesData.select().where(GamesData.Age == choice):
        query_games_ages += [age.Name]  # Добавление имени из базы данных в список запросов
        ids += [age.id]  # Добавление идентификатора из базы данных в список идентификаторов

    inline_keyboard_filters_ages = get_inline_keyboard_filters_age()  # Получение встроенной клавиатуры фильтров по возрасту

    # Проверка, если встроенная клавиатура есть, возвращаем ее, иначе уменьшаем текущую страницу и повторно получаем клавиатуру
    if inline_keyboard_filters_ages is not None:
        return inline_keyboard_filters_ages
    else:
        current_page -= 1  # Уменьшение текущей страницы на 1
        inline_keyboard_filters_ages = get_inline_keyboard_filters_age()  # Получение встроенной клавиатуры фильтров по возрасту

    return inline_keyboard_filters_ages  # Возвращаем встроенную клавиатуру


# Обработчик нажатия кнопки "prev" в inline клавиатуре фильтров по возрасту
@rate_limit(limit=3)  # Применение декоратора для ограничения количества вызовов функции
@dp.callback_query_handler(text="prev",
                           state=SwitchMenu.Filters_ages_after_inline)  # Регистрация обработчика для кнопки "prev"
async def handle_prev_page(callback_query: types.CallbackQuery):
    global current_page, query_games_ages, ids  # Использование глобальных переменных
    if current_page > 1:
        current_page -= 1  # Уменьшение текущей страницы на 1

    inline_keyboard_filters_ages = get_inline_keyboard_filters_age()  # Получение встроенной клавиатуры фильтров по возрасту

    # Попытка изменить встроенную клавиатуру сообщения
    try:
        if inline_keyboard_filters_ages is not None:
            await callback_query.message.edit_reply_markup(
                reply_markup=inline_keyboard_filters_ages)  # Изменение встроенной клавиатуры
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось


# Обработчик нажатия кнопки "next" в inline клавиатуре фильтров по возрасту
@rate_limit(limit=3)  # Применение декоратора для ограничения количества вызовов функции
@dp.callback_query_handler(text="next",
                           state=SwitchMenu.Filters_ages_after_inline)  # Регистрация обработчика для кнопки "next"
async def handle_next_page(callback_query: types.CallbackQuery):
    global current_page, query_games_ages, ids  # Использование глобальных переменных
    current_page += 1  # Увеличение текущей страницы на 1

    inline_keyboard_filters_ages = get_inline_keyboard_filters_age()  # Получение встроенной клавиатуры фильтров по возрасту

    # Попытка изменить встроенную клавиатуру сообщения
    try:
        if inline_keyboard_filters_ages is not None:
            await callback_query.message.edit_reply_markup(
                reply_markup=inline_keyboard_filters_ages)  # Изменение встроенной клавиатуры
    except MessageNotModified:
        pass  # Просто игнорируем ошибку, если сообщение не изменилось
