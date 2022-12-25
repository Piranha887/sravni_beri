from bot.utils.set_default_bot_commands import set_default_commands


async def on_startup(dp):
    from bot import filters
    from bot import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from bot.utils import on_startup_notify

    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

