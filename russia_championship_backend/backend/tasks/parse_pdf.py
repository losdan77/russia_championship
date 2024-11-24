import re
from datetime import datetime

def get_indices(lst, target):
    return [i for i, x in enumerate(lst) if x == target]

def remove_by_indices(lst, indices):
    return [x for i, x in enumerate(lst) if i not in indices]

def find_name_sport(lst):
  pattern = r'^(?=.*[А-ЯЁ])([А-ЯЁ]+(-[А-ЯЁ]+)*)( [А-ЯЁ]+(-[А-ЯЁ]+)*)*$'
  sport = []
  for i in range(len(lst)):
    if lst[i] in sp:
      if lst[i] not in sport:
        sport.append(lst[i])
      
  return sport

def index_sport(sport,lst):
  ind_dict = dict()
  for i in sport:
    temp = lst
    ind_dict[i] = temp.index(i)
    temp = temp[temp.index(i)+1:]
  return ind_dict

def remove_str(lst):
  pattern = r'Стр. \d+ из \d+' 
  filtered_result = [s for s in lst if s and not re.fullmatch(pattern, s)]
  return filtered_result

def is_valid_date(date_string):
    try:
        # Попробуем преобразовать строку в дату
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False

def searching_for_indexes_between_competitions(data, index):
  pattern = r'\b\d{16}\s+[А-ЯЁ]+'
  indices = []
  count = 0
  start_index = index
  indices = []
  for index in range(start_index, len(data)):
      item = data[index]
      if re.search(pattern, item):
          indices.append(index)  # Добавляем индекс в список
          count += 1  # Увеличиваем счетчик
          if count == 2:  # Проверяем, достигли ли мы второго вхождения
              break  # Останавливаем цикл

  return [i for i in range(indices[0], indices[1])]


def is_integer(string):
    try:
        int(string)  # Попытка преобразовать строку в целое число
        return True
    except ValueError:
        return False


def start_sport_list(filtered_result,name_sport):
  sp = 'Авиамодельный спорт; Авиационные гонки; Автомобильный спорт; Айкидо; Акробатический рок-н-ролл; Альпинизм; Американский футбол; Армрестлинг; Бадминтон; Баскетбол; Бейсбол; Биатлон; Бильярдный спорт; Бобслей; Бодибилдинг; Бокс; Борьба на поясах; Боулинг; Брейкинг; Велосипедный спорт; Вертолетный спорт; Водно-моторный спорт; Водное поло; Воднолыжный спорт; Воздухоплавательный спорт; Воздушная гимнастика; Воздушно-силовая атлетика; Волейбол; Восточное боевое единоборство; Всестилевое каратэ; Гандбол; Гиревой спорт; Го; Гольф; Гонки дронов (беспилотных воздушных судов); Гонки с препятствиями; Горнолыжный спорт; Городошный спорт; Гребля на байдарках и каноэ; Гребной слалом; Гребной спорт; Дартс; Джиу-джитсу; Дзюдо; Ездовой спорт; Зимнее плавание; Каратэ; Кендо; Кёрлинг; Кикбоксинг; Кинологический спорт; Киокусинкай; Киокушин; Компьютерный спорт; Конный спорт; Конькобежный спорт; Корэш; Кудо; Лапта; Легкая атлетика; Лыжное двоеборье; Лыжные гонки; Микрофутзал; Многоборье готов к труду и обороне; Морское многоборье; Мотоциклетный спорт; Муайтай; Нарды; Настольный теннис; Падел; Парашютный спорт; Парусный спорт; Пауэрлифтинг; Перетягивание каната; Пилонный спорт; Плавание; Планерный спорт; Подводный спорт; Полиатлон; Практическая стрельба; Прыжки в воду; Прыжки на батуте; Прыжки на лыжах с трамплина; Пулевая стрельба; Пэйнтбол; Радиоспорт ; Рафтинг; Регби; Роллер спорт; Роуп скиппинг (спортивная скакалка); Рукопашный бой; Рыболовный спорт; Сават; Самбо; Самолетный спорт; Санный спорт; Северное многоборье; Серфинг; Силовой экстрим; Синхронное плавание; Скалолазание; Сквош; Скейтбординг; Смешанное боевое единоборство (ММА); Сноуборд; Современное пятиборье; Софтбол; Спорт сверхлегкой авиации; Спортивная борьба; Спортивно-прикладное собаководство; Спортивное метание ножа; Спорт глухих; Спорт лиц с интеллектуальными нарушениями; Спорт лиц с поражением ОДА; Спорт слепых; Спортивная акробатика; Спортивная аэробика; Спортивная гимнастика; Спортивное ориентирование; Спортивное программирование; Спортивный туризм; Стендовая стрельба; Страйкбол; Стрельба из арбалета; Стрельба из лука; Стрельба на дальние дистанции; Судомодельный спорт; Сумо; Танцевальный спорт; Теннис; Триатлон; Тхэквондо; Тхэквондо ГТФ; Тхэквондо ИТФ; Тхэквондо МФТ; Тяжелая атлетика; Универсальный бой; Ушу; Фехтование; Фигурное катание на коньках ; Фиджитал спорт (функционально-цифровой спорт); Фитнес-аэробика; Флорбол; Фристайл; Функциональное многоборье; Футбол; Футбол лиц с заболеванием ЦП; Хапкидо; Хоккей; Хоккей на траве; Хоккей с мячом; Художественная гимнастика; Чир спорт; Шахматы; Шашки; Эстетическая гимнастика'
  sp.upper()
  sp = sp.split(';')
  sp = [(x.upper()).lstrip() for x in sp]

  stran = "Австралия, Австрия, Азербайджан, Албания, Алжир, Ангола, Андорра, Антигуа и Барбуда, Аргентина, Армения, Афганистан, Багамские Острова, Бангладеш, Барбадос, Бахрейн, Белиз, Белоруссия, Бельгия, Бенин, Болгария, Боливия, Босния и Герцеговина, Ботсвана, Бразилия, Бруней, Буркина-Фасо, Бурунди, Бутан, Вануату, Ватикан, Великобритания, Венгрия, Венесуэла, Восточный Тимор, Вьетнам, Габон, Гаити, Гайана, Гамбия, Гана, Гватемала, Гвинея, Гвинея-Бисау, Германия, Гренада, Греция, Грузия, Дания, Джибути, Доминика, Доминиканская Республика, Демократическая Республика Конго, Египет, Замбия, Зимбабве, Израиль, Индия, Индонезия, Иордания, Ирак, Иран, Ирландия, Исландия, Испания, Италия, Йемен, Кабо-Верде, Казахстан, Камбоджа, Камерун, Канада, Катар, Кения, Кипр, Киргизия (Кыргызстан), Кирибати (Кирибати), Китай (Китайская Народная Республика), Северная Корея (КНДР), Колумбия (Колумбия), Коморские Острова (Коморы), Коста-Рика (Коста-Рика), Берег Слоновой Кости (Кот-д'Ивуар), Куба (Куба), Кувейт (Кувейт), Лаос (Лаос), Латвия (Латвия), Лесото (Лесото), Либерия (Либерия), Ливан (Ливан), Ливия (Ливия), Литва (Литва), Лихтенштейн (Лихтенштейн), Люксембург (Люксембург), Маврикий (Маврикий), Мавритания (Мавритания), Мадагаскар (Мадагаскар), Малави (Малави), Малайзия (Малайзия), Мали (Мали), Мальдивы (Мальдивы), Мальта (Мальта), Марокко (Марокко), Маршалловы Острова (Маршалловы Острова), Мексика (Мексика), Мозамбик (Мозамбик), Молдавия (Молдова), Монако (Монако), Монголия (Монголия), Мьянма (Бирма), Намибия (Намибия), Науру (Науру), Непал (Непал), Нигер (Нигер), Нигерия (Нигерия), Нидерланды (Нидерланды), Никарагуа (Никарагуа), Новая Зеландия (Новая Зеландия), Норвегия (Норвегия), Объединенные Арабские Эмираты (ОАЭ), Оман (Оман), Пакистан (Пакистан), Палау (Палау), Панама (Панама), Папуа - Новая Гвинея (Папуа - Новая Гвинея), Парагвай (Парагвай), Перу (Перу), Польша (Польша), Португалия (Португалия), Республика Конго (Республика Конго), Южная Корея  (Южная Корея или Корея Республиканская) , Россия , Руанда , Румыния , Сальвадор , Самоа , Сан-Марино , Сан-Томе и Принсипи , Саудовская Аравия , Северная Македония , Сейшельские Острова , Сенегал , Сент-Винсент и Гренадины , Сент-Китс и Невис , Сент-Люсия , Сербия , Сингапур , Сирия , Словакия , Словения , Соломоновы Острова , Сомали , Судан , Суринам , Соединенные Штаты Америки , Сьерра-Леоне , Таджикистан , Таиланд , Танзания , Того , Тонга , Тринидад и Тобаго , Тувалу , Тунис , Туркмения , Турция , Уганда , Узбекистан , Украина , Уругвай , Федеративные Штаты Микронезии , Фиджи , Филиппины , Финляндия , Франция , Хорватия , Центральноафриканская Республика  (ЦАР)  (Центральноафриканская Республика)  (ЦАР)  (Центральноафриканская Республика)  (ЦАР)  (Центральноафриканская Республика)  (ЦАР)  (Центральноафриканская Республика)  (ЦАР)  (Центральноафриканская Республика)  (ЦАР)  (Центральноафриканская Республика)  (ЦАР)  (Центральноафриканская Республика)  (ЦАР) Чад Черногория Чехия Чили Швейцария Швеция Шри-Ланка Эквадор Экваториальная Гвинея Эритрея Эсватини Эстония Эфиопия Южноафриканская Республика Ямайка Япония."
  stran = stran.split(',')
  stran = [x.strip() for x in stran]
  stran[stran.index('Белоруссия')] = 'Беларусь'
  stran = [x.upper() for x in stran]
  stran_rem = []
  for i in stran:
    if len(i.split('('))>1:
      stran_rem.append(' '.join(i.split('(')[:len(i.split('('))-1]))
    else:
      stran_rem.append(i)
  stran_rem = [x.rstrip() for x in stran_rem]
  stran_rem = stran_rem[:-1]

  count = 1
  sport_list = []
  start_date_index = 0
  country_index = 0
  sport_name = find_name_sport(result)
  sport_index = index_sport(sport_name,filtered_result)
  name_sport = name_sport

  max_id = 0
  i = 0
  delet = 0
  ocr = 0
  while i <= len(filtered_result) - 1:
    name_champ = ''
    start_date = ''
    end_date = ''
    country = ''
    city = ''
    subjetc = ''
    description = ''
    number_of_participants = ''
    age_group = ''
    subject = ''
    id = ''
    text = filtered_result[i]
    if filtered_result[i-1] in sport_index.keys():
      name_sport = filtered_result[i-1]
      i += 1
      continue
    if count == 1:
      name_sport = name_sport
      if re.search(r'\d+ [А-ЯЁ]+', text):
        try:
          range_id = searching_for_indexes_between_competitions(filtered_result, i)
        except:
          range_id = [x for x in range(max_id+1,len(filtered_result))]
        max_id = max(range_id)
        rem_id = [x for x in range_id]
        date = 1
        age_group = ''
        for t in range_id:
          # Поиск 1 строки
          if re.search(r'\d{16} [А-ЯЁ]+', filtered_result[t]):
            spl = filtered_result[t].split()
            id = spl[0]
            name_champ = ' '.join(spl[1:])
            rem_id.remove(t)
            ocr = 1
            if (re.search(r'.*ОКРУГ+', filtered_result[t + 1]) and ocr == 1):
              name_champ += ' ' + filtered_result[t + 1]
              rem_id.remove(t+1)
          # Поиск 2 и 3 строки
          if is_valid_date(filtered_result[t]):
            if date == 1:
              start_date = filtered_result[t]
              rem_id.remove(t)
            if date == 2:
              end_date = filtered_result[t]
              rem_id.remove(t)
            date = 2
          # Поиск 4 строки
          if filtered_result[t] in stran_rem:
            country = filtered_result[t]
            rem_id.remove(t)
          # Поиск 5 строки
          if re.search(r'(?<!\S)([Гг]\.?\s+[А-Яа-яЁё]+)(?!\s*\d)', filtered_result[t]):
            if not re.search(r'\b[A-ZА-ЯЁ]+\s+[Гг]\.', filtered_result[t]):
              if not re.search(r'\.\s*[Гг]\.', filtered_result[t]):
                try:
                  subject, city = filtered_result[t].split(',')
                  rem_id.remove(t)
                except:
                  city = filtered_result[t]
                  subject = 'None'
                  rem_id.remove(t)
            try:
              if filtered_result[t + 1] == 'Мансийск':
                city += 'Мансийск'
                rem_id.remove(t)
                continue
            except:
              pass
          if re.search(r'\bпоселок\b', filtered_result[t]):
            try:
              if re.search(r'\bНИЖЕГОРОДСКАЯ ОБЛАСТЬ\b', filtered_result[t-1]):
                subject, city = filtered_result[t-1].split(',')
                rem_id.remove(t-1)
                city += '  '+filtered_result[t]
              else:
                subject, city = filtered_result[t].split(',')
                rem_id.remove(t)
            except:
              city += filtered_result[t]
              subject = 'None'
              try:
                rem_id.remove(t)
              except:
                pass
            if re.search(r'\bгородского типа\b', filtered_result[t+1]):
                city += ' '+ filtered_result[t+1]
                delet = 1
                continue
          if re.search(r'\bпоселение\b', filtered_result[t]):
            try:
              subject, city = filtered_result[t].split(',')
              rem_id.remove(t)
            except:
              city = filtered_result[t]
              subject = 'None'
              try:
                rem_id.remove(t)
              except:
                pass
          if re.search(r'\село\b', filtered_result[t]):
            try:
              subject, city = filtered_result[t].split(',')
              rem_id.remove(t)
            except:
              city = filtered_result[t]
              subject = 'None'
              try:
                rem_id.remove(t)
              except:
                pass
          if re.search(r'\деревня\b', filtered_result[t]):
            try:
              subject, city = filtered_result[t].split(',')
              rem_id.remove(t)
            except:
              city = filtered_result[t]
              subject = 'None'
              rem_id.remove(t)
          if re.search(r'^\b[А-ЯЁA-Z][а-яёa-z]+\b$', filtered_result[t]):
            if filtered_result[t] == 'Мансийск':
              rem_id.remove(t)
            else:
              try:
                subject, city = filtered_result[t].split(',')
                rem_id.remove(t)
              except:
                city += filtered_result[t]
                subject = 'None'
                try:
                  rem_id.remove(t)
                except:
                  pass
          if re.search(r'\b[A-Z][a-z]+\b', filtered_result[t]):
            try:
              subject, city = filtered_result[t].split(',')
              rem_id.remove(t)
            except:
              city += filtered_result[t]
              subject = 'None'
              try:
                rem_id.remove(t)
              except:
                pass
          # Поиск 6 строки
          if is_integer(filtered_result[t]):
            number_of_participants = filtered_result[t]
            rem_id.remove(t)
          # Поиск 7 строки
          if re.search(r'\s*(женщины|мужчины|юниоры|юниорки|юноши|мальчики|девочки|девушки|до \d{1,2} лет)\s*',
                      filtered_result[t]):
            age_group += ' ' + filtered_result[t]
            rem_id.remove(t)
          if delet == 1:
            rem_id.remove(t)
            delet = 0
        if len(rem_id) != 0:
          description = ' '.join([filtered_result[x] for x in rem_id if filtered_result[x] not in sp])
        else:
          descriptoin = ''
        i = max_id + 1
        sport = {
          'id': id,
          'name_sport': name_sport,
          'name_champ': name_champ,
          'start_date': start_date,
          'end_date': end_date,
          'country': country,
          'city': city.lstrip(),
          'subjetc': subject,
          'number_of_participants': number_of_participants,
          'age_group': [x.lstrip() for x in age_group.split(',')],
          'description': [x.lstrip() for x in description.split(',')]
        }
        count = 1
        sport_list.append(sport)
        sport.clear

      else:
        i+=1
  return sport_list, name_sport

def main(count_page):
  '''
  для запуска  
  на вход: количество страниц
  выход: список словарей для дальнейшего формирования json файла
  '''
  name_sport = ''
  EKP = list()
  for i in range(2494):
    c = 0
    print(i)
    result = ''.join(data[f'Page_{i}'][4])
    result = result.split('\n')
    if i == 0:
      result = result[19:] # Использовать на 1 страницы (Page_0)
    num = get_indices(result, 'Основной состав')
    result = remove_by_indices(result,num)
    sport_name = find_name_sport(result)
    pattern = r'Стр. \d+ из \d+' 
    filtered_result = ''
    filtered_result = [s for s in result if s and not re.fullmatch(pattern, s)]
    sport_index = index_sport(sport_name,filtered_result)
    sport_list, name_sport_t = start_sport_list(filtered_result, name_sport, sport_index)
    if name_sport_t:
      name_sport = name_sport_t
    EKP+=sport_list
  return EKP