from aiogram import executor

from loader import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.main_db import create_db
from handlers.register_handlers import (
    register_handlers_echo,
    register_handlers_admin,
)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # register handlers
    register_handlers_echo(dp)
    register_handlers_admin(dp)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    create_db()
    executor.start_polling(dp, on_startup=on_startup)

