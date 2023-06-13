# Импорт необходимых модулей и классов
import re  # Импорт модуля re (регулярные выражения)
from aiogram import types  # Импорт классов types из модуля aiogram
from aiogram.dispatcher.filters import BoundFilter  # Импорт класса BoundFilter из модуля aiogram.dispatcher.filters


# Создание класса AgeCheck, наследующегося от класса BoundFilter
class AgeCheck(BoundFilter):
    # Метод check для проверки возраста в сообщении
    async def check(self, message: types.Message):
        try:
            pattern = re.compile(r"^\d{1,2}[+]$")  # Задание шаблона для регулярного выражения
            return message.text == pattern.match(message.text).group(
                0)  # Проверка соответствия текста сообщения шаблону
        except:
            await message.answer("Нажмите на кнопку в меню")  # Отправка ответного сообщения, если возникла ошибка
            return False  # Возвращение False, если возникла ошибка
