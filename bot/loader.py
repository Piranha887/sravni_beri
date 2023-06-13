# Импорт необходимых модулей и классов
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Импорт конфигурационных данных
from bot.data import config

# Создание экземпляров бота, хранилища и диспетчера
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определение списка экспортируемых переменных
__all__ = ["bot", "storage", "dp"]
