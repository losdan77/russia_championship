from aiogram import Bot
from aiogram.types import Message
from core.dao.user import UserDAO
from core.keyboards.main import main_keyboard
from aiogram.fsm.context import FSMContext
from core.utils.state_register import StepsRegister


async def get_start(message: Message, state: FSMContext):
    username = message.from_user.first_name

    # test_data = await UserDAO.select()

    hello_text = f'''
                    Привет, <b>{username}</b>, это бот который присылает уведомления о событиях, пришли своей email через который ты зарегестрирован на сайте, чтобы получать свои уведомления 
                '''
    
    await message.answer(hello_text,
                         parse_mode='HTML')
    await state.set_state(StepsRegister.GET_EMAIL)
    
    # for _ in test_data:
    #     await message.answer(str(_))