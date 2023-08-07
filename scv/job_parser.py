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
            list_vacancy.extend(item)
        return response_json

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
        return response_json

class WorkingWithVacancies:
    """
    класс для работы с вакансиями
    """
    def __init__(self, name: str, url: str, requirements: str, pay: int):
        self.name = name
        self.url = url
        self.pay = pay
        self.requirements = requirements

    def __repr__(self):
        return f'_{__class__.__name__}("{self.name}","{self.url}","{self.requirements}",{self.pay})'

    def __str__(self):
        """
        информация для пользователя
        """
        return f'Название фирмы: {self.name},\nCсылка на вакансию: {self.url},\nТребования: {self.requirements},\nОплата от {self.pay} рублей'

    @classmethod
    def sj_vacancy(cls, list_vacancys, search_quantity):
        list_vacancy = []
        for object in list_vacancys["objects"]:
            try:
                name = object['client']['title']
                if name == None or "":
                    name = "название фирмы не указано"
                url = object['client']['url']
                if url == None or "":
                    url = "ссылка на вакансию не указана"
                requirements = object['candidat']
                if requirements == None or "":
                   requirements = "требований нет"
                pay = int(object['payment_from'])
                if pay == None:
                    pay = 0
                list_vacancy.append(cls(name, url, requirements, pay))
            except:
                ""
        if list_vacancy == []:
            return "по данному запросу ничего не найдено"
        return list_vacancy[0:search_quantity]

    @classmethod
    def hh_vacancy(cls, list_vacancys):
        list_vacancy = []
        for item in list_vacancys['items']:
            try:
                name = item['employer']['name']
                if name == None or "":
                    name = "название фирмы не указано"
                url = item['employer']['url']
                if url == None or "":
                    url = "ссылка на вакансию не указана"
                requirements = f"{item['experience']['name']}, {item['employment']['name']}"
                if requirements == None or "":
                   requirements = "требований нет"
                pay = int(item['salary']['from'])
                if pay == None:
                    pay = 0
                list_vacancy.append(cls(name, url, requirements, pay))
            except:
                ""
        if list_vacancy == []:
            return "по данному запросу ничего не найдено"
        return list_vacancy

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


