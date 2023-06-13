# Импорт необходимых модулей и классов
from typing import List, Any
from aiogram.types import ReplyKeyboardMarkup
from write_in_database import Buttons


# Определение функции для разделения списка на подсписки фиксированного размера
def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# Определение функции для создания клавиатуры фильтров по возрасту
def keyboard_filters_age():
    # Получение списка кнопок фильтров возраста из базы данных
    query_ages = [age.age_buttons for age in Buttons.select()]

    # Разделение списка значений кнопок на строки (по 4 кнопки в каждой строке)
    lines_filters_age: List[List[Any]] = list(partition(query_ages, 4))

    # Создание списка кнопок клавиатуры
    keyboard_buttons = []
    for line in lines_filters_age:
        keyboard_buttons.append(line)

    # Добавление кнопки "Фильтры" в конец списка
    keyboard_buttons.append(['\U0001f519 Фильтры'])

    # Создание объекта клавиатуры с заданными кнопками
    keyboard_filters_ages = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True)
    return keyboard_filters_ages  # Возврат созданной клавиатуры
