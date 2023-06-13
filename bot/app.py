import os
import asyncpg
from aiogram import Dispatcher
from aiogram.types import ChatMemberStatus
from bot.keyboards.default import keyboard_start
from bot.states import SwitchMenu


async def get_user_list():
    # Устанавливаем соединение с базой данных
    conn = await asyncpg.connect(
        host='localhost',
        user=str(os.getenv("PGUSER")),
        password=str(os.getenv("PGPASSWORD")),
        database=str(os.getenv("DATABASE"))
    )

    try:
        # Выполняем SQL-запрос для получения списка пользователей
        query = 'SELECT id FROM users'
        users = await conn.fetch(query)
        user_list = [user['id'] for user in users]
        return user_list
    finally:
        # Закрываем соединение с базой данных
        await conn.close()


async def on_startup(dp: Dispatcher):
    # Получаем список пользователей из базы данных
    users = await get_user_list()

    for user_id in users:
        try:
            # Получаем информацию о пользователе
            chat_member = await dp.bot.get_chat_member(user_id, user_id)

            # Проверяем статус пользователя
            if chat_member.status != ChatMemberStatus.KICKED:
                # Отправляем сообщение только, если пользователь не заблокировал бота
                await dp.bot.send_message(user_id, 'Бот Включён')
                await dp.bot.send_message(user_id, "Нажмите кнопку из главного меню", reply_markup=keyboard_start)
                await dp.current_state(user=user_id).set_state(SwitchMenu.Main)
            else:
                # print(f"Пользователь {user_id} заблокировал бота.")
                pass
        except Exception as e:
            # print(f"Ошибка при отправке сообщения пользователю {user_id}: {str(e)}.")
            pass


async def on_shutdown(dp: Dispatcher):
    # Получаем список пользователей из базы данных
    users = await get_user_list()

    for user_id in users:
        try:
            # Отправляем сообщение о выключении бота
            await dp.bot.send_message(user_id, 'Бот Выключён')
        except Exception as e:
            # print(f"Ошибка при отправке сообщения пользователю {user_id}: {str(e)}.")
            pass


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers import dp

    # Запускаем бота с обработчиками on_startup и on_shutdown
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
