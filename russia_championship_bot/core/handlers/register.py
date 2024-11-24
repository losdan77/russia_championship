import smtplib
import random
from aiogram import Bot
from aiogram.types import Message
from core.dao.user import UserDAO
from core.keyboards.main import main_keyboard
from aiogram.fsm.context import FSMContext
from config import settings
from email.message import EmailMessage
from core.utils.state_register import StepsRegister

async def get_email(message: Message, state: FSMContext):
    email = message.text

    try:
        user = await UserDAO.find_by(email=email)
    

        new_code = random.randint(100000, 999999)

        await UserDAO.update_by_id(id = user['id'],
                                   single_mode_code = str(new_code))    

        try:
            msg_content = new_code

            msg = EmailMessage()
            msg.set_content(f'Одноразовый код для доступа: {msg_content}', charset='utf-8')
            msg['Subject'] = 'Одноразовый код'
            msg['From'] = settings.SMTP_USER
            msg['To'] = email

            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
                server.starttls()
                server.login(settings.SMTP_USER, settings.SMTP_PASS)
                server.send_message(msg)
        except:
            pass
        
        await message.answer('Теперь введите одноразовый код, который пришел Вам на почту')
        await state.update_data(email = message.text)
        await state.set_state(StepsRegister.GET_CODE)
    except:
        await message.answer('Нет такого пользователя')


async def verify_code(message: Message, state: FSMContext):
    try:
        telegram_id = message.from_user.id
        code_in_db = await UserDAO.find_by(single_mode_code = message.text)
        
            
        await UserDAO.update_by_id(id = code_in_db['id'],
                                telegram_id = str(telegram_id))
        await message.answer('Теперь вы будете получать уведомления!')
        await state.clear()
    except:
        await message.answer('Неверный код')