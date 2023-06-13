import logging

from aiogram import Dispatcher

from bot.data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Сообщение для администраторов: Бот Запущен и готов к работе")

        except Exception as err:
            logging.exception(err)

