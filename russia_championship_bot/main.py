import asyncio
from aiogram import Bot, Dispatcher, F
from config import settings
from core.handlers.base import start_bot, stop_bot
from core.handlers.start import get_start

async def start():
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()


    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start,
                        F.text == '/start')


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())