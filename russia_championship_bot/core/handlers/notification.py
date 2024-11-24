from datetime import datetime
from aiogram import Bot
from aiogram.types import Message
from core.dao.user import UserDAO
from config import settings
from core.dao.event import EventsNotificationDAO, EventsDAO, TypeChampionshipDAO


async def mailing(bot: Bot):
    today_date = (datetime.now()).date()
    today_notification = await EventsNotificationDAO.check_notification(today_date=today_date)
    if not today_notification:
        return None

    for notification in today_notification:
        try:
            event = await EventsDAO.find_by(id = notification['event_id'])
            user = await UserDAO.find_by(id = notification['user_id'])
            type_championship = await TypeChampionshipDAO.find_by(id = event['id_type_championship'])
        
            msg_content = f'Напоминание: {type_championship['type_name']} произойдет {event['date_start']}'

            await bot.send_message(chat_id=int(user['telegram_id']),
                                   text=msg_content)
        except:
            continue