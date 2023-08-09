import pytest

from scv.job_parser import HHCollectingVacancies, WorkingWithVacancies

@pytest.fixture
def fixture_test_search_vacancy_hh():
    HH = HHCollectingVacancies()
    vac = HH.search_vacancy("python", 1)
    return vac

@pytest.fixture
def fixture_ww_hh():
    vac = []
    return vac

@pytest.fixture
def fixture_ww_sj_list():
    vac = []
    return vac

@pytest.fixture
def fixture_ww_sj():
    vac = {"objects":[{'client': {'title': "Яндекс", 'url': "www.ya.ru"},'candidat': "чтоб руки были", 'payment_from': 2000}]}
    return vac

@pytest.fixture
def fixture_test_WW_search_hh():
    return {'alternate_url': 'https://hh.ru/search/vacancy?area=113&enable_snippets=true&items_on_page=8&text=python',
 'arguments': None,
 'clusters': None,
 'found': 10259,
 'items': [{'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': {'building': '33с1',
                        'city': 'Москва',
                        'description': None,
                        'id': '11188205',
                        'lat': 55.703515,
                        'lng': 37.696705,
                        'metro': {'lat': 55.706156,
                                  'line_id': '10',
                                  'line_name': 'Люблинско-Дмитровская',
                                  'lng': 37.68544,
                                  'station_id': '10.52',
                                  'station_name': 'Кожуховская'},
                        'metro_stations': [{'lat': 55.706156,
                                            'line_id': '10',
                                            'line_name': 'Люблинско-Дмитровская',
                                            'lng': 37.68544,
                                            'station_id': '10.52',
                                            'station_name': 'Кожуховская'}],
                        'raw': 'Москва, 2-й Южнопортовый проезд, 33с1',
                        'street': '2-й Южнопортовый проезд'},
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84826929',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84826929',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-08-09T12:49:42+0300',
            'department': None,
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/865',
                         'id': '865',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/2655142.png',
                                       '90': 'https://hhcdn.ru/employer-logo/2655141.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/553417.png'},
                         'name': 'TerraLink',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/865',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=865'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
            'has_test': True,
            'id': '84826929',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Стажер-разработчик Python',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-09T12:49:42+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': 'Аналитический склад ума, быстрая '
                                       'обучаемость. Знание '
                                       '<highlighttext>Python</highlighttext>, '
                                       'SQL на уровне выборок данных из '
                                       'нескольких таблиц \\ insert \\ update, '
                                       'хорошие знания Excel...',
                        'responsibility': 'Обучение профессии Разработчик '
                                          '<highlighttext>Python</highlighttext> '
                                          'в проектах под руководством '
                                          'наставника по индивидуальному плану '
                                          'и включение в Программу развития.'},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84826929?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84841138',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84841138',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-08-09T15:18:57+0300',
            'department': {'id': '816144-816144-office',
                           'name': 'ВкусВилл. Офис'},
            'employer': {'accredited_it_employer': False,
                         'alternate_url': 'https://hh.ru/employer/816144',
                         'id': '816144',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/4154421.jpeg',
                                       '90': 'https://hhcdn.ru/employer-logo/4154420.jpeg',
                                       'original': 'https://hhcdn.ru/employer-logo-original/928465.jpg'},
                         'name': 'ВкусВилл',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/816144',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=816144'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '84841138',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Исследователь данных, удаленно',
            'premium': False,
            'professional_roles': [{'id': '10', 'name': 'Аналитик'}],
            'published_at': '2023-08-09T15:18:57+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': {'currency': 'RUR',
                       'from': 190000,
                       'gross': False,
                       'to': None},
            'schedule': None,
            'snippet': {'requirement': 'Умение слышать реальные боли '
                                       'заказчика. — Знание статистики, '
                                       'математического анализа, теории '
                                       'вероятностей, линейной алгебры. — '
                                       'Понимание бизнес-метрик. — Уверенные '
                                       'знание SQL (составление...',
                        'responsibility': 'Выявлять скрытые тенденции и '
                                          'закономерности, описывать их в том '
                                          'числе в виде аналитических '
                                          'материалов. — Проведение ad-hoc '
                                          'исследований. — '},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84841138?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': {'building': '6В',
                        'city': 'Санкт-Петербург',
                        'description': None,
                        'id': '2430909',
                        'lat': 59.914637,
                        'lng': 30.416399,
                        'metro': None,
                        'metro_stations': [],
                        'raw': 'Санкт-Петербург, Октябрьская набережная, 6В',
                        'street': 'Октябрьская набережная'},
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84742357',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84742357',
            'archived': False,
            'area': {'id': '2',
                     'name': 'Санкт-Петербург',
                     'url': 'https://api.hh.ru/areas/2'},
            'contacts': None,
            'created_at': '2023-08-08T14:46:36+0300',
            'department': None,
            'employer': {'accredited_it_employer': False,
                         'alternate_url': 'https://hh.ru/employer/3942275',
                         'id': '3942275',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/2953833.jpeg',
                                       '90': 'https://hhcdn.ru/employer-logo/2953832.jpeg',
                                       'original': 'https://hhcdn.ru/employer-logo-original/628170.jpg'},
                         'name': 'Миторра',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/3942275',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3942275'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '84742357',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Full Stack разработчик (Junior+)',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-08T14:46:36+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': 'Знание HTML, CSS и JavaScript. Базовое '
                                       'знание серверных языков '
                                       'программирования: PHP, '
                                       '<highlighttext>Python</highlighttext>. '
                                       'Разработка анимации с помощью HTML5, '
                                       'JavaScript, jQuery. ',
                        'responsibility': 'Разработка и поддержка '
                                          'пользовательского интерфейса '
                                          'веб-сайтов с использованием HTML, '
                                          'CSS и JavaScript. Разработка '
                                          'интерактивных интерфейсов на JS. '},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84742357?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/83690278',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=83690278',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-07-19T13:53:35+0300',
            'department': None,
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/4903713',
                         'id': '4903713',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/3743376.png',
                                       '90': 'https://hhcdn.ru/employer-logo/3743375.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/825622.png'},
                         'name': 'Диалог Регионы',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/4903713',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4903713'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '83690278',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Backend разработчик (Python)',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-07-19T13:53:35+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': 'Опыт работы с FastAPI или Django, '
                                       'Flask. Умения работать с '
                                       'PostgreSQL/MySQL. Опыт работы с '
                                       'многопоточностью, асинхронностью. '
                                       'Знания основных паттернов...',
                        'responsibility': 'Интеграция c внешними сервисами. '
                                          'Обработка больших объемов данных. '
                                          'Планирование архитектурных решений. '
                                          'Работа с высоконагруженными и '
                                          'отказоустойчивыми сервисами. '
                                          'Применение гибких методологий...'},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/83690278?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84630964',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84630964',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-08-07T09:41:55+0300',
            'department': None,
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/4872201',
                         'id': '4872201',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/6020774.png',
                                       '90': 'https://hhcdn.ru/employer-logo/6020773.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/1100040.png'},
                         'name': 'ANABAR',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/4872201',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4872201'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
            'has_test': False,
            'id': '84630964',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Разработчик Python (junior)',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-07T09:41:55+0300',
            'relations': [],
            'response_letter_required': True,
            'response_url': None,
            'salary': {'currency': 'RUR',
                       'from': None,
                       'gross': True,
                       'to': 80000},
            'schedule': None,
            'snippet': {'requirement': 'Знание что такое swagger. Знание как '
                                       'управлять зависимостями в приложениях '
                                       'на '
                                       '<highlighttext>python</highlighttext> '
                                       '(pip/poetry/pipenv). Понимание про '
                                       'typehints/mypy. ',
                        'responsibility': 'Написание микросервисов для '
                                          'аналитических сервисов (формируют '
                                          'хитрый оптимизированный запрос в '
                                          'БД, обрабатывает на '
                                          '<highlighttext>python</highlighttext> '
                                          'и отдает в '
                                          '<highlighttext>python</highlighttext>). '},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84630964?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84724735',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84724735',
            'archived': False,
            'area': {'id': '66',
                     'name': 'Нижний Новгород',
                     'url': 'https://api.hh.ru/areas/66'},
            'contacts': None,
            'created_at': '2023-08-08T11:54:57+0300',
            'department': None,
            'employer': {'accredited_it_employer': False,
                         'alternate_url': 'https://hh.ru/employer/139',
                         'id': '139',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/3381258.png',
                                       '90': 'https://hhcdn.ru/employer-logo/3381257.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/735070.png'},
                         'name': 'IBS',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/139',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=139'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
            'has_test': False,
            'id': '84724735',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Стажер-разработчик Python',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-08T11:54:57+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': '...программированию баз данных и '
                                       'другим направлениям IT. Знание SQL и '
                                       'языка '
                                       '<highlighttext>Python</highlighttext>. '
                                       'Знание Excel. Системное мышление и '
                                       'аналитический склад ума/.',
                        'responsibility': 'Участие в разработке систем на '
                                          '<highlighttext>Python</highlighttext>.'},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84724735?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84853609',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84853609',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-08-09T17:53:49+0300',
            'department': {'id': '2367681-2367681-dev',
                           'name': 'BI.ZONE Направление Разработка'},
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/2367681',
                         'id': '2367681',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/4253437.png',
                                       '90': 'https://hhcdn.ru/employer-logo/4253436.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/953226.png'},
                         'name': 'BI.ZONE',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/2367681',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2367681'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '84853609',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Junior Python Developer',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-09T17:53:49+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': 'Умение писать на '
                                       '<highlighttext>Python</highlighttext> '
                                       '(>3). Знание django/drf. Умение '
                                       'работать с git или другой системой '
                                       'контроля версий. Умение написать '
                                       'Dockerfile...',
                        'responsibility': 'Принимать участие в разработке '
                                          'нескольких продуктов в области '
                                          'кибер-безопасности. Участвовать в '
                                          'проектировании новых возможностей '
                                          'наших платформ. Современная '
                                          'техника. '},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84853609?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': True,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84494321',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84494321',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-08-03T14:00:47+0300',
            'department': None,
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/6150428',
                         'id': '6150428',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/5694001.png',
                                       '90': 'https://hhcdn.ru/employer-logo/5694000.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/1018308.png'},
                         'name': 'Ит-Финанс',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/6150428',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=6150428'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '84494321',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Тестировщик/Manual QA инженер',
            'premium': False,
            'professional_roles': [{'id': '124', 'name': 'Тестировщик'}],
            'published_at': '2023-08-03T14:00:47+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': {'currency': 'RUR',
                       'from': None,
                       'gross': False,
                       'to': 100000},
            'schedule': None,
            'snippet': {'requirement': 'Опыт работы с bugtracking-системами. '
                                       'Опыт работы с Postman PostgreSQL. '
                                       'Базовые знание '
                                       '<highlighttext>Python</highlighttext>. '
                                       'Selenium/Playwright или другой '
                                       'инструмент для автоматизации...',
                        'responsibility': 'Проводить ручное тестирование '
                                          'нового функционала внутренней '
                                          'системы, выполнять регрессионное '
                                          'тестирование, usability. Активное '
                                          'участие в проработке требований как '
                                          'для уже существующих...'},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84494321?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []}],
 'page': 0,
 'pages': 250,
 'per_page': 8}



@pytest.fixture
def fixture_test_search_vacancy_hh():
    return {'alternate_url': 'https://hh.ru/search/vacancy?area=113&enable_snippets=true&items_on_page=3&text=python',
 'arguments': None,
 'clusters': None,
 'found': 10118,
 'items': [{'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84630964',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84630964',
            'archived': False,
            'area': {'id': '1',
                     'name': 'Москва',
                     'url': 'https://api.hh.ru/areas/1'},
            'contacts': None,
            'created_at': '2023-08-07T09:41:55+0300',
            'department': None,
            'employer': {'accredited_it_employer': True,
                         'alternate_url': 'https://hh.ru/employer/4872201',
                         'id': '4872201',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/6020774.png',
                                       '90': 'https://hhcdn.ru/employer-logo/6020773.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/1100040.png'},
                         'name': 'ANABAR',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/4872201',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4872201'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
            'has_test': False,
            'id': '84630964',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Разработчик Python (junior)',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-07T09:41:55+0300',
            'relations': [],
            'response_letter_required': True,
            'response_url': None,
            'salary': {'currency': 'RUR',
                       'from': None,
                       'gross': True,
                       'to': 80000},
            'schedule': None,
            'snippet': {'requirement': 'Знание что такое swagger. Знание как '
                                       'управлять зависимостями в приложениях '
                                       'на '
                                       '<highlighttext>python</highlighttext> '
                                       '(pip/poetry/pipenv). Понимание про '
                                       'typehints/mypy. ',
                        'responsibility': 'Написание микросервисов для '
                                          'аналитических сервисов (формируют '
                                          'хитрый оптимизированный запрос в '
                                          'БД, обрабатывает на '
                                          '<highlighttext>python</highlighttext> '
                                          'и отдает в '
                                          '<highlighttext>python</highlighttext>). '},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84630964?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': True,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84519177',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84519177',
            'archived': False,
            'area': {'id': '2',
                     'name': 'Санкт-Петербург',
                     'url': 'https://api.hh.ru/areas/2'},
            'contacts': None,
            'created_at': '2023-08-03T21:19:51+0300',
            'department': None,
            'employer': {'accredited_it_employer': False,
                         'alternate_url': 'https://hh.ru/employer/10143876',
                         'id': '10143876',
                         'logo_urls': None,
                         'name': 'Стоян Игнатий Вадимович',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/10143876',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10143876'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
            'has_test': False,
            'id': '84519177',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Начинающий программист (стажер) разработчик Python - '
                    'парсинг сайтов',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-03T21:19:51+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': 'Желательно знание основ парсинга '
                                       'сайтов и баз данных, '
                                       '<highlighttext>python</highlighttext>. '
                                       'Обязательно базовые знания ООП, SQL, '
                                       'CSS (понимание селекторов). Базовое '
                                       'понимание HTTP...',
                        'responsibility': None},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84519177?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []},
           {'accept_incomplete_resumes': False,
            'accept_temporary': False,
            'address': None,
            'adv_response_url': None,
            'alternate_url': 'https://hh.ru/vacancy/84713587',
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=84713587',
            'archived': False,
            'area': {'id': '66',
                     'name': 'Нижний Новгород',
                     'url': 'https://api.hh.ru/areas/66'},
            'contacts': None,
            'created_at': '2023-08-08T10:10:25+0300',
            'department': None,
            'employer': {'accredited_it_employer': False,
                         'alternate_url': 'https://hh.ru/employer/2888',
                         'id': '2888',
                         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/546156.png',
                                       '90': 'https://hhcdn.ru/employer-logo/546155.png',
                                       'original': 'https://hhcdn.ru/employer-logo-original/232219.bmp'},
                         'name': 'DSSL',
                         'trusted': True,
                         'url': 'https://api.hh.ru/employers/2888',
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2888'},
            'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '84713587',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Python разработчик',
            'premium': False,
            'professional_roles': [{'id': '96',
                                    'name': 'Программист, разработчик'}],
            'published_at': '2023-08-08T10:10:25+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': None,
            'schedule': None,
            'snippet': {'requirement': 'Опыт коммерческой разработки на '
                                       '<highlighttext>Python</highlighttext> '
                                       'от 1 года. Базовое знание JavaScript. '
                                       'Опыт работы с React. Базовое знание '
                                       'HTML, CSS, вёрстки. ',
                        'responsibility': 'Разработка нового функционала для '
                                          'платформы работы с видеоаналитикой. '
                                          'Разработка аналитических модулей '
                                          'для платформы. Решение интересных '
                                          'архитектурных задач. Проведение '
                                          'code review. '},
            'sort_point_distance': None,
            'type': {'id': 'open', 'name': 'Открытая'},
            'url': 'https://api.hh.ru/vacancies/84713587?host=hh.ru',
            'working_days': [],
            'working_time_intervals': [],
            'working_time_modes': []}],
 'page': 0,
 'pages': 666,
 'per_page': 3}









