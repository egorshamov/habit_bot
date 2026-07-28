"""
Habit Bot

Главный файл запуска приложения.
"""

import asyncio

from app.bot import bot, dp


async def main() -> None:
    """
    Запуск Telegram-бота.
    """

    print("🚀 Habit Bot запускается")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())