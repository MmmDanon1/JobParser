from pprint import pprint

from scv.job_parser import HHCollectingVacancies, SuperJobCollectingVacancies


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    platforms = ["HeadHunter", "SuperJob"]
    while True:
        user_input = input(f'Здравствуйте! Какую будем использовать платформу для поиска вакансий {" or ".join(platforms)}:')
        if user_input == platforms[0]:
            if user_input == platforms[0]:
                search_query = input(f"Искать будем на платформе: {platforms[0]}. Введите поисковый запрос: ")
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                if top_n > 100:
                    print("не могу вывести более 100 вакансий =(")
                else:
                    HH = HHCollectingVacancies()
                    pprint(HH.search_vacancy(search_query, top_n))
                    break

        elif user_input == platforms[1]:
            if user_input == platforms[1]:
                search_query = input(f"Искать будем на платформе: {platforms[1]}. Введите поисковый запрос: ")
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                if top_n > 100:
                    print("не могу вывести более 100 вакансий =(")
                else:
                    SJ = SuperJobCollectingVacancies()
                    sorted_list = input("Отсортировать список вакансий по оплате от большего к меньшему? (yes/no)")
                    if sorted_list == "yes":
                        pass
                    pprint(SJ.search_vacancy(search_query, top_n))
                    break

if __name__ == "__main__":
    user_interaction()