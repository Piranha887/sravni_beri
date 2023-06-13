# Импорт необходимых модулей и классов
import asyncio  # Импорт модуля asyncio для асинхронной работы
from aiogram import types, Dispatcher  # Импорт классов types, Dispatcher из модуля aiogram
from aiogram.dispatcher import DEFAULT_RATE_LIMIT  # Импорт константы DEFAULT_RATE_LIMIT из модуля aiogram.dispatcher
from aiogram.dispatcher.handler import CancelHandler, \
    current_handler  # Импорт классов CancelHandler, current_handler из модуля aiogram.dispatcher.handler
from aiogram.dispatcher.middlewares import \
    BaseMiddleware  # Импорт класса BaseMiddleware из модуля aiogram.dispatcher.middlewares
from aiogram.utils.exceptions import Throttled  # Импорт класса Throttled из модуля aiogram.utils.exceptions


# Создание класса ThrottlingMiddleware, наследующегося от класса BaseMiddleware
class ThrottlingMiddleware(BaseMiddleware):

    # Метод инициализации класса
    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit  # Установка предела скорости
        self.prefix = key_prefix  # Установка префикса ключа
        super(ThrottlingMiddleware, self).__init__()

    # Асинхронный метод, вызываемый при обработке сообщения
    # noinspection PyUnusedLocal
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()  # Получение текущего обработчика
        dispatcher = Dispatcher.get_current()  # Получение текущего диспетчера
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)  # Получение предела скорости обработчика
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")  # Получение ключа обработчика
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)  # Применение ограничения скорости
        except Throttled as t:
            await self.message_throttled(message, t)  # Обработка ограничения скорости
            raise CancelHandler()  # Отмена обработчика

    # Асинхронный метод для обработки ограничения скорости сообщения
    async def message_throttled(self, message: types.Message, throttled: Throttled):
        handler = current_handler.get()  # Получение текущего обработчика
        dispatcher = Dispatcher.get_current()  # Получение текущего диспетчера
        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")  # Получение ключа обработчика
        else:
            key = f"{self.prefix}_message"
        delta = throttled.rate - throttled.delta  # Вычисление временной разницы
        if throttled.exceeded_count <= 4:
            await message.reply('Too many requests! ')  # Отправка ответного сообщения о превышении лимита
        await asyncio.sleep(delta)  # Асинхронная задержка
        thr = await dispatcher.check_key(key)  # Проверка ключа
        if thr.exceeded_count == throttled.exceeded_count:
            await message.reply('Unlocked.')  # Отправка ответного сообщения о разблокировке
