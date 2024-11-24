import json
from fastapi import APIRouter, Depends
from datetime import datetime, timedelta
from backend.event.dao import CountrysDAO, CityDAO, SexDAO, EventsDAO, DisciplineDAO
from backend.event.dao import TypeChampionshipDAO, TypeSportDAO, SubjectsDAO
from backend.event.dao import EventsDisciplineDAO, EventsSexDAO, EventsNotificationDAO
from backend.event.schemas import SFilter, SSubscribe
from backend.tasks.tasks import dump_in_db, parse_pdf_from_website
from backend.exception import StartEndDateException, NoPermitException
from backend.user.models import User
from backend.user.dependecies import get_current_user

router = APIRouter(
    prefix='/events',
    tags=['События']
)


@router.get('/all_countrys')
async def get_all_countrys():
    countrys = await CountrysDAO.find_all()
    return countrys


@router.get('/all_subjects')
async def get_all_subjects():
    subjects = await SubjectsDAO.find_all()
    return subjects


@router.get('/all_subjects_in_country')
async def get_all_subjects_in_country(id_country: int):
    subjects = await SubjectsDAO.find_all(id_country = id_country)
    return subjects


@router.get('/all_city')
async def get_all_city():
    city = await CityDAO.find_all()
    return city


@router.get('/all_city_in_subject')
async def get_all_city_in_subject(id_subject: int):
    city = await CityDAO.find_all(id_subject = id_subject)
    return city


@router.get('/all_sex')
async def get_all_sex():
    sex = await SexDAO.find_all()
    return sex


@router.get('/all_type_championship')
async def get_all_type_championship():
    type_championship = await TypeChampionshipDAO.find_all()
    return type_championship


@router.get('/all_type_sport')
async def get_all_type_sport():
    type_sport = await TypeSportDAO.find_all()
    return type_sport


@router.get('/all_discipline')
async def get_all_discipline():
    discipline = await DisciplineDAO.find_all()
    return discipline


@router.get('/all_count_values')
async def get_all_count_values():
    count = await EventsDAO.find_all_count_values()
    return count


@router.post('/all_events_with_filters')
async def get_all_events_with_filters(filter_data: SFilter):
    city_list = None
    type_championship_name_list = None
    type_sport_name_list = None
    sex_name_list = None
    discipline_name_list = None
    count_list = None
    print(filter_data.type_sport_name)
    if filter_data.date_start and filter_data.date_end:
        if filter_data.date_start > filter_data.date_end:
            raise StartEndDateException

    if filter_data.city:
        city_list = [c.strip() for c in filter_data.city.split(',')]
    if filter_data.type_championship_name:
        type_championship_name_list = [tc.strip() for tc in filter_data.type_championship_name.split(',')]
    if filter_data.type_sport_name:
        type_sport_name_list = [ts.strip() for ts in filter_data.type_sport_name.split(',')]
    if filter_data.sex_name:
        sex_name_list = [s.strip() for s in filter_data.sex_name.split(',')]
    if filter_data.discipline_name:
        discipline_name_list = [d.strip() for d in filter_data.discipline_name.split(',')]
    if filter_data.count_values:
        count_list = [co.strip() for co in filter_data.count_values.split(',')]
    
    events = await EventsDAO.find_all(subject = filter_data.subject,
                                      city = city_list,
                                      type_championship_name = type_championship_name_list,
                                      type_sport_name = type_sport_name_list,
                                      sex_name = sex_name_list,
                                      discipline_name = discipline_name_list,
                                      count_values = count_list,
                                      date_start = filter_data.date_start,
                                      date_end = filter_data.date_end,)
    return events


@router.get('/event_by_id')
async def get_event_by_id(event_id: str):
    event = await EventsDAO.find_one(event_id = event_id)
    return event


@router.post('/subscribe_notification')
async def add_sudcribe_notification(subscribe_data: SSubscribe,
                                    current_user: User = Depends(get_current_user)):
    start_date = await EventsDAO.find_by(id = subscribe_data.event_id)
    date_start = start_date['date_start']
    date_notification = date_start - timedelta(days=subscribe_data.count_day)
    
    if date_notification < (datetime.now()).date():
        raise StartEndDateException
    try:
        notification = await EventsNotificationDAO.add(event_id = subscribe_data.event_id,
                                                    user_id = current_user['id'],
                                                    count_days = date_notification,)
        return notification
    except:
        raise NoPermitException
    


@router.get('/dump_json_to_db')
async def dump_json_to_db():
    dump_in_db.delay()


@router.get('/parse_pdf_from_website')
async def get_parse_pdf_from_website():
    parse_pdf_from_website.delay()


@router.get('/compare_json')
async def compare_json():
    class CompareJson:
        """
        Класс для сравнения двух файлов на изменение
        """
        def load_json(self, file_path):
            """
            Метод для загрузки данных из JSON файла
            :return: json файл в виде python словаря
            """
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)


        def compare(self, old_data, new_data):
            """
            Метод для сравнения двух списков словарей
            :param old_data: старый файл
            :param new_data: новый файл с изменениями
            :return: список изменений
            """
            changes = []

            # Преобразование старых данных во множество для быстрого поиска
            new_data_set = {json.dumps(item, sort_keys=True) for item in new_data}

            for item in old_data:
                item_str = json.dumps(item, sort_keys=True)
                if item_str not in new_data_set:
                    changes.append(item)

            return changes


    old_file_path = 'data_Full_copy.json'  # Путь к первому файлу
    new_file_path = 'data_Full.json'  # Путь ко второму файлу
    output_file_path = 'changes.json'  # Путь к выходному файлу

    compare_json = CompareJson()

    # Загружаем данные из файлов
    old_data = compare_json.load_json(old_file_path)
    new_data = compare_json.load_json(new_file_path)

    # Сравниваем данные и получаем изменения
    changes = compare_json.compare(old_data, new_data)

    # Сохраняем изменения в новый JSON файл
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(changes, output_file, ensure_ascii=False, indent=4)
        
@router.get('/check')
async def check_notifications():
    today_date = (datetime.now()).date()
    return await EventsNotificationDAO.check_notification(today_date=today_date)


