# Импорт необходимых модулей и классов
from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from peewee import *
from bot.data import config
from write_in_database import Buttons


# Определение функции для разделения списка на подсписки фиксированного размера
def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# Определение функции для создания клавиатуры библиотеки
def keyboard_library():
    # Подключение к базе данных PostgreSQL
    db = PostgresqlDatabase(database=config.DATABASE, user=config.PGUSER, password=config.PGPASSWORD, host=config.ip)

    # Получение списка значений кнопок библиотеки из базы данных
    query_symbol = []
    for tag in Buttons.select():
        query_symbol += [tag.library_buttons]

    # Разделение списка значений кнопок на строки (по 6 кнопок в каждой строке)
    lines_library: List[Any] = list(partition(query_symbol, 6))

    # Создание списка строк кнопок клавиатуры
    keyboard_lines = []
    for line in lines_library:
        keyboard_lines.append(line)

    # Добавление кнопки "Главное меню" в конец списка строк
    keyboard_lines.append(['\U0001f519 Главное меню'])

    # Создание объекта клавиатуры с заданными строками кнопок
    keyboard_library = ReplyKeyboardMarkup(
        keyboard=keyboard_lines,
        resize_keyboard=True
    )
    return keyboard_library  # Возврат созданной клавиатуры
