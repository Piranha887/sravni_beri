# Импорт необходимых модулей и классов
import os  # Импорт модуля os для работы с операционной системой
import re  # Импорт модуля re (регулярные выражения)
import asyncpg  # Импорт модуля asyncpg для работы с PostgreSQL базой данных
from aiogram import types  # Импорт классов types из модуля aiogram
from aiogram.dispatcher.filters import BoundFilter  # Импорт класса BoundFilter из модуля aiogram.dispatcher.filters


# Создание класса ManufactoryCheck, наследующегося от класса BoundFilter
class ManufactoryCheck(BoundFilter):
    # Метод check для проверки типа производителя в сообщении
    async def check(self, message: types.Message):
        try:
            pattern = re.compile(r"^(?!(🔙\sФильтры|🔙\sНазад)$).*")  # Задание шаблона для регулярного выражения

            if message.text == pattern.match(message.text).group(0):  # Проверка соответствия текста сообщения шаблону
                # Подключение к базе данных
                connection = await asyncpg.connect(
                    database=os.getenv("DATABASE"),  # Получение значения переменной окружения DATABASE
                    user=os.getenv("PGUSER"),  # Получение значения переменной окружения PGUSER
                    password=os.getenv("PGPASSWORD"),  # Получение значения переменной окружения PGPASSWORD
                    host='localhost'  # Установка значения хоста подключения
                )

                # Проверка значения в базе данных
                query = "SELECT manufacture_buttons FROM buttons WHERE manufacture_buttons = $1"
                result = await connection.fetchval(query, message.text)
                await connection.close()

                if result:  # Если значение найдено в базе данных
                    return True
                else:
                    await message.answer(
                        "Нажмите на кнопку в меню")  # Отправка ответного сообщения, если значение не найдено
                    return False
            else:
                await message.answer(
                    "Нажмите на кнопку в меню")  # Отправка ответного сообщения, если текст не соответствует шаблону
                return False
        except:
            await message.answer("Нажмите на кнопку в меню")  # Отправка ответного сообщения, если возникла ошибка
            return False
