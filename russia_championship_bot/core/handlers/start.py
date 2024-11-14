from aiogram import Bot
from aiogram.types import Message
from core.dao.user import UserDAO

async def get_start(message: Message, bot: Bot):
    username = message.from_user.first_name

    test_data = await UserDAO.select()

    hello_text = f'''
                    Привет, <b>{username}</b> 
                '''
    # await message.answer(hello_text,
    #                     #  reply_markup=main_keyboard,
    #                      parse_mode='HTML',)
    
    for _ in test_data:
        await message.answer(str(_))