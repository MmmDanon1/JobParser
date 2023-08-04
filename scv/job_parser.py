import json
import os
from pprint import pprint

import requests
from abc import ABC, abstractmethod

class CollectingVacancies(ABC):
    """
    абстрактный класс для работы с API сайтов с вакансиями
    """
    @abstractmethod
    def search_vacancy(self, keyword: str, search_quantity: int):
        pass

class HHCollectingVacancies(CollectingVacancies):
    """
    класс для работы с API сайтов с вакансиями на платформе hh.ru
    """
    url_hh = "https://api.hh.ru/vacancies"

    def search_vacancy(self, keyword: str, search_quantity: int):
        params_hh = {"text": keyword,
                     "area": 113,
                     "page": 0,
                     "per_page": search_quantity
                     }
        response = requests.get(url=HHCollectingVacancies.url_hh, params=params_hh)
        response_json = response.json()
        list_vacancy = []
        for item in response_json['items']:
            try:
                name = item['employer']['name']
                url = item['employer']['url']
                requirements = item['experience']['name'], item['employment']['name']
                pay = item['salary']['from']
                list_vacancy.extend([{"name": name, "url": url, "requirements": requirements, "pay": pay}])
            except:
                ""
        if list_vacancy == []:
            return "по данному запросу ничего не найдено"
        return list_vacancy

class SuperJobCollectingVacancies(CollectingVacancies):
    """
    класс для работы с API сайтов с вакансиями на платформе superjob.ru
    """
    SK_SJ = os.getenv("SK_SJ")
    url_sj = "https://api.superjob.ru/2.0/vacancies"
    def search_vacancy(self, keyword: str, search_quantity: int):
        '''
        получение списка словарей вакансий по имени, урлу, требованиям и зарплате
        :param keyword:
        :return:[{}]
        '''
        headers_hh = {"X-Api-App-Id": SuperJobCollectingVacancies.SK_SJ}
        params_hh = {"keyword": keyword,
                     }
        response = requests.get(url=SuperJobCollectingVacancies.url_sj, headers=headers_hh, params=params_hh)
        response_json = response.json()
        list_vacancy = []
        for object in response_json["objects"]:
            try:
                name = object['client']['title']
                url = object['client']['url']
                requirements = object['candidat']
                pay = object['payment_from']
                list_vacancy.extend([{"name": name, "url": url, "requirements": requirements, "pay": pay}])
            except:
                ""
        if list_vacancy == []:
            return "по данному запросу ничего не найдено"
        return list_vacancy[0:search_quantity]


class WorkingWithVacancies:
    """
    класс для работы с вакансиями
    """
    def __init__(self, name: str, url: str, requirements: str, pay: int):
        self.name = name
        self.url = url
        self.pay = pay
        self.requirements = requirements

    def __str__(self):
        """
        информация для пользователя
        """
        return f'Название фирмы: {self.name},\nCсылка на вакансию: {self.url},\nТребования: {self.requirements},\nОплата от {self.pay} рублей'

    def __add__(self, other):
        """
        сравниваtn два канала между собой по числу подписчиков (сложение)
        """
        return self.pay + other.pay

    def __sub__(self, other):
        """
        сравниваtn два канала между собой по числу подписчиков (вычитание)
        """
        return self.pay - other.pay

    def __lt__(self, other):
        """
        сравниваtn два канала между собой по числу подписчиков (меньше ли)
        """
        return self.pay < other.pay

    def __le__(self, other):
        """
        сравниваtn два канала между собой по числу подписчиков (меньше или ровно)
        """
        return self.pay <= other.pay

    def __gt__(self, other):
        """
        сравниваtn два канала между собой по числу подписчиков (больше ли)
        """
        return self.pay > other.pay

    def __ge__(self, other):
        """
        сравниваtn два канала между собой по числу подписчиков (больше или ровно)
        """
        return self.pay >= other.pay

    @classmethod
    def job_selection(cls, list_vacancy: list[dict]):
        """
        метод сравнения вакансий по зарплате
        :return: вакансия с максимальной оплатой
        """
        sorted_list_vacancy = sorted(list_vacancy, key=lambda x: x['pay'], reverse=True)
        for list in sorted_list_vacancy[0:1]:
            name = str(list["name"])
            url = str(list['url'])
            requirements = str(list['requirements'])
            pay = int(list['pay'])

        return cls(name, url, requirements, pay)

    def salary_vacancies(self, list_vacancy: list[dict]) -> list[dict]:
        """
        метод сравнения вакансий по зарплате
        :return: список вакансий отсортированных по оплате
        """
        sorted_list_vacancy = sorted(list_vacancy, key=lambda x: x['pay'], reverse=True)
        return sorted_list_vacancy

WW = WorkingWithVacancies(1, 2, 2, 3)
print()
# print(WW.job_selection([{"name": "1", "url": "2", "requirements": '3', "pay": 4}, {"name": "1", "url": "2", "requirements": "3", "pay": 5}, {"name": "1", "url": "2", "requirements": "3", "pay": 6}]))
# print(WorkingWithVacancies("1", "2", "3", 4))
pprint(WW.salary_vacancies([{"name": "1", "url": "2", "requirements": '3', "pay": 4},
                           {"name": "1", "url": "2", "requirements": "3", "pay": 5},
                           {"name": "1", "url": "2", "requirements": "3", "pay": 7},
                           {"name": "2", "url": "2", "requirements": "3", "pay": 3}]))
class SaveVacancies(ABC):
    """
    абстрактный класс для работы с сохранением вакансий в файл
    """
    pass

    @abstractmethod
    def add_json(self, list_vacancy):
        """
        метод довавления вакансий в json-файл
        :return: json-файл
        """
        pass

    @abstractmethod
    def get_vacancies(self):
        """
        получение вакансий из json-файла
        :return: вакансии из json-файла
        """
        pass

    @abstractmethod
    def delete_vacancies(self):
        """
        удаление вакансий с json-файла
        :return:
        """
        pass


class JsonSaveVacancies(SaveVacancies):
    """
    класс для сохранения информации о вакансиях в JSON-файл.
    """

    def add_json(self, list_vacancy):
        """
        метод довавления вакансий в json-файл
        :param **kwargs:
        :return: json-файл
        """
        with open('vacancy.json', 'w') as f:
            json.dump([list_vacancy], f)

    def get_vacancies(self):
        """
        получение вакансий из json-файла
        :return: вакансии из json-файла
        """
        with open('vacancy.json', 'r') as f:
            data = json.load(f)
        return data

    def delete_vacancies(self):
        """
        удаление вакансий с json-файла
        :return:
        """
        open('vacancy.json', 'w').close()


