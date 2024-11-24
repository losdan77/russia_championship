import asyncio
from aiogram import Bot, Dispatcher, F
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import settings
from core.handlers.base import start_bot, stop_bot
from core.handlers.start import get_start
from core.handlers.register import get_email, verify_code
from core.handlers.notification import mailing
from core.utils.state_register import StepsRegister

async def start():
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()


    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(mailing,
                      trigger='cron',
                      hour=10,
                      minute=0,
                      kwargs={'bot': bot})
    # scheduler.add_job(mailing,
    #                   trigger='interval',
    #                   seconds=20,
    #                   kwargs={'bot': bot})
    scheduler.start()


    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start,
                        F.text == '/start')
    
    dp.message.register(get_email,
                        StepsRegister.GET_EMAIL)
    dp.message.register(verify_code,
                        StepsRegister.GET_CODE)
    
    # dp.message.register(mailing,
    #                     F.text == '/test')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())