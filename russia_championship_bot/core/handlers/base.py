from aiogram import Bot
from aiogram.types import Message, BotCommand, BotCommandScopeDefault, FSInputFile
from aiogram.enums import parse_mode
from config import settings

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start',
                   description='Начало работы'),
        BotCommand(command='help',
                   description='Помощь с ботом'),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.ADMIN_ID, 'Бот запущен!',
                           parse_mode='HTML')


async def stop_bot(bot: Bot):
    users_info = FSInputFile(path=r'./users.txt')
    # await bot.send_document(ADMIN_ID, document=users_info)
    await bot.send_message(settings.ADMIN_ID, 'Бот остановлен!')