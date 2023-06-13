# Импорт необходимых модулей и классов
import os  # Модуль для работы с операционной системой
from aiogram import types  # Импорт типов и классов aiogram
from aiogram.dispatcher.filters.builtin import CommandStart  # Импорт фильтра для команды /start
from peewee import PostgresqlDatabase, DoesNotExist, Model, IntegerField  # Импорт классов для работы с базой данных
from bot.keyboards.default import keyboard_start  # Импорт клавиатуры
from bot.loader import dp  # Импорт экземпляра диспетчера
from bot.states import SwitchMenu  # Импорт состояния
from bot.utils.misc import rate_limit  # Импорт декоратора для ограничения частоты запросов

# Подключение к базе данных PostgreSQL
db = PostgresqlDatabase(
    database=os.getenv("DATABASE"),  # Имя базы данных из переменной окружения
    user=os.getenv("PGUSER"),  # Имя пользователя из переменной окружения
    password=os.getenv("PGPASSWORD"),  # Пароль пользователя из переменной окружения
    host='localhost'  # Хост базы данных
)


# Определение модели пользователя
class User(Model):
    id = IntegerField(primary_key=True)  # Поле id пользователя

    class Meta:
        database = db  # Использование созданной базы данных
        table_name = 'users'  # Имя таблицы в базе данных


# Создание таблицы, если она еще не существует
db.create_tables([User], safe=True)


# Обработчик команды /start
@rate_limit(limit=10)  # Ограничение частоты выполнения команды
@dp.message_handler(CommandStart())  # Обработка команды /start
async def bot_start(message: types.Message):  # Функция-обработчик команды /start
    user_id = message.from_user.id  # Идентификатор пользователя

    try:
        # Поиск пользователя в базе данных
        user = User.get_by_id(user_id)
        await message.answer(f'Привет, {message.from_user.full_name}!')  # Ответ пользователю
    except DoesNotExist:
        # Создание нового пользователя
        user = User(id=user_id)
        user.save(force_insert=True)
        # await message.answer(f'Привет, {message.from_user.full_name}! Ты был добавлен в базу данных.')

    await message.answer("Нажмите кнопку из меню ниже", reply_markup=keyboard_start)  # Ответ пользователю с клавиатурой
    await SwitchMenu.Main()  # Переход к состоянию SwitchMenu.Main()
