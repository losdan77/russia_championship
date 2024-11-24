#celery -A backend.tasks.celery_app:celery worker --loglevel=INFO
import boto3
import smtplib
import fake_useragent
import requests
import json
import os
import urllib3
from datetime import datetime
from bs4 import BeautifulSoup
from email.message import EmailMessage
from asgiref.sync import async_to_sync
from backend.tasks.celery_app import celery
from backend.config import settings
from backend.event.dao import CountrysDAO, CityDAO, SexDAO, EventsDAO
from backend.event.dao import TypeChampionshipDAO, TypeSportDAO, SubjectsDAO
from backend.event.dao import EventsDisciplineDAO, EventsSexDAO, DisciplineDAO
from backend.event.dao import EventsNotificationDAO
from backend.user.dao import UserDAO
from backend.tasks.parse_pdf import main

urllib3.disable_warnings()

async def dump_json_to_db():
    with open('data_Full.json', 'r') as file:
        data = json.load(file)
    
    for line in data:

        try:
            country = await CountrysDAO.find_by(country_name = line['country'])
            if not country:
                
                country = await CountrysDAO.add(country_name = line['country'])
                
        except:
            continue

        try:
            subject = await SubjectsDAO.find_by(subject_name = line['subjetc'])
            if not subject:
                subject = await SubjectsDAO.add(subject_name = line['subjetc'],
                                                    id_country = country['id'])
            
        except:
                continue

        try:
            city = await CityDAO.find_by(city_name = line['city'])
            if not city:    
            
                city = await CityDAO.add(city_name = line['city'],
                                        id_subject = subject['id'])
                city = city['id']
            city = city['id']
        except:
                continue

        
        try:
            type_sport = await TypeSportDAO.find_by(type_name = line['name_sport'])
            if not type_sport:
                
                type_sport = await TypeSportDAO.add(type_name = line['name_sport'])
                type_sport = type_sport['id']
                
            type_sport = type_sport['id']
        except:
                continue

        try:        
            type_championship = await TypeChampionshipDAO.find_by(type_name = line['name_champ'])
            if not type_championship:
                
                type_championship = await TypeChampionshipDAO.add(type_name = line['name_champ'])
                type_championship = type_championship['id']
                
            type_championship = type_championship['id']
        except:
                continue

        for word in line['age_group']:
            sex = await SexDAO.find_by(sex = word)
            if not sex:
                try:
                    sex = await SexDAO.add(sex = word)
                    sex = sex['id']
                except:
                    continue

        for word in line['description']:
            discipline = await DisciplineDAO.find_by(discipline_name = word)
            if not discipline:
                try:
                    discipline = await DisciplineDAO.add(discipline_name = word)
                    discipline = discipline['id']
                except:
                    continue
        try:
            event = await EventsDAO.find_by(id = line['id'])
            if not event:
                
                    date_start = datetime.strptime(line['start_date'], '%d.%m.%Y')
                    date_end = datetime.strptime(line['end_date'], '%d.%m.%Y')
                    event = await EventsDAO.add(id = line['id'],                                           
                                                date_start = date_start,
                                                date_end = date_end,
                                                count = line['number_of_participants'],                                         
                                                id_type_championship = type_championship,
                                                id_type_sport = type_sport,
                                                id_city = city,)
                    event = event['id']
                
            event = event['id']
        except:
                continue
    
        for word in line['age_group']:
            sex = await SexDAO.find_by(sex = word)
            try:
                sex = sex['id']
                events_sex = await EventsSexDAO.add(event_id = event,
                                                    sex_id = sex)
            except Exception as e:
                print(e)
                continue

        for word in line['description']:
            descipline = await DisciplineDAO.find_by(discipline_name = word)
            try:
                descipline = descipline['id']
                events_descipline = await EventsDisciplineDAO.add(event_id = event,
                                                                  discipline_id = descipline)
            except:
                continue

    return 'ok'


class DownloadFile:
    """
    Класс для парсинга страницы https://www.minsport.gov.ru/activity/government-regulation/edinyj-kalendarnyj-plan/
    и загрузки единого календарного плана за каждый год
    """
    def __init__(self):
        self.__user_agent = fake_useragent.UserAgent()
        self.__fake_ua = {'user-agent': self.__user_agent.random}
        self.__url = 'https://www.minsport.gov.ru/activity/government-regulation/edinyj-kalendarnyj-plan/'
        self.__sub_string = 'Единый календарный план межрегиональных, всероссийских и международных физкультурных мероприятий и спортивных мероприятий'

    def get_page(self):
        """
        Метод для получения страницы в json формате
        :return: страница в json формате
        """
        try:
            response = requests.get(self.__url, verify=False, headers=self.__fake_ua)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            try:
                next_data_script = soup.find('script', id='__NEXT_DATA__')
                json_data = next_data_script.string
                data = json.loads(json_data)
                return data
            except Exception as e:
                raise e

        except Exception as e:
            raise e

    def search_second_part_ekp(self, data):
        """
        Метод для поиска блока с необходимыми нам документами
        :param data: страница
        :return: блок с необходимыми нам документами
        """
        for item in data['props']['pageProps']['sections']:
            if item['title'] == 'II часть ЕКП':
                second_part_ekp = item
        return second_part_ekp

    def search_title_and_url(self, second_part_ekp):
        """
        :param second_part_ekp: блок с необходимыми нам документами
        :return files: словарь ключ: название файла, значение: ссылка на файл
        """
        files = {}
        for item in second_part_ekp['documents']:
            if self.__sub_string in item['attributes']['title']:
                url = item['attributes']['file']['data']['attributes']['url']
                title = url.rsplit('/', 1)[-1]
                files[title] = url
        return files

    @staticmethod
    def check_for_file_changes(filename):
        """
        Статический метод для проверки изменения файла
        :param file: название файла
        :return: True or False
        """
        if os.path.exists(filename):
            return True
        else: return False

    def download_file(self, filename, url):
        """
        :param files: словарь с файлами
        :return: None
        """
        with requests.get(url, stream=True, verify=False, headers=self.__fake_ua) as r:
            r.raise_for_status()
            with open(f'{filename}', 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)


@celery.task
def send_new_password_on_email(email: str,
                               new_code: str):
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


@celery.task
def dump_in_db():
    async_to_sync(dump_json_to_db)()


@celery.task(name = 'dump_in_db_scheduler')
def dump_in_db_scheduler():
    async_to_sync(dump_json_to_db)()
    

@celery.task(name = 'parse_pdf_from_website')
def parse_pdf_from_website():
    download = DownloadFile()
    page = download.get_page()
    second_part_ekp = download.search_second_part_ekp(page)
    files = download.search_title_and_url(second_part_ekp)
    for filename, url in files.items():
        if download.check_for_file_changes(filename):
            continue
        download.download_file(filename, url)


@celery.task
def upload_profile_image(file_path: str,
                         id_profile: int):
    
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=settings.ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.REGION_NAME
    )

    s3.upload_file(file_path, 
              settings.BACKET_NAME, 
              f'{id_profile}_profile.jpg')
    

async def check_notifications():
    today_date = (datetime.now()).date()
    return await EventsNotificationDAO.check_notification(today_date=today_date)


async def event_info(event_id: str):
    return await EventsDAO.find_by(id = event_id)


async def user_info(user_id: str):
    return await UserDAO.find_by(id = user_id)


async def type_championship_info(id: str):
    return await TypeChampionshipDAO.find_by(id = id)


@celery.task(name = 'notificate_in_email')
def notificate_in_email():
    today_notification = async_to_sync(check_notifications)()
    if not today_notification:
        return None

    for notification in today_notification:
        
            event = async_to_sync(event_info)(event_id=notification['event_id'])
            user = async_to_sync(user_info)(user_id=notification['user_id'])
            type_championship = async_to_sync(type_championship_info)(id = event['id_type_championship'])
        
            msg_content = f'{type_championship['type_name']} произойдет {event['date_start']}'
        
            msg = EmailMessage()
            msg.set_content(f'Напоминание: {msg_content}', charset='utf-8')
            msg['Subject'] = 'Напоминание о событии'
            msg['From'] = settings.SMTP_USER
            msg['To'] = user['email']

     
            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
                server.starttls()
                server.login(settings.SMTP_USER, settings.SMTP_PASS)
                server.send_message(msg)
     

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


@celery.task(name = 'compare_json')
def compare_json():
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


@celery.task(name = 'pdf_parse')
def pdf_parse():
    data = main()
    with open('data.json', 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
