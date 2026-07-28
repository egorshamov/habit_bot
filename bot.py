"""
Главный модуль Habit Bot.

Создание бота и подключение всех обработчиков.
"""

from aiogram import Bot, Dispatcher

from app.config.settings import settings

from app.handlers import start
from app.handlers import catalog
from app.handlers import habits
from app.handlers import profile
from app.handlers import statistics


def create_bot() -> Bot:
    """
    Создание Telegram бота.
    """

    return Bot(
        token=settings.BOT_TOKEN
    )


def create_dispatcher() -> Dispatcher:
    """
    Создание диспетчера и подключение роутеров.
    """

    dp = Dispatcher()

    # Подключение обработчиков
    dp.include_router(start.router)
    dp.include_router(catalog.router)
    dp.include_router(habits.router)
    dp.include_router(profile.router)
    dp.include_router(statistics.router)

    return dp