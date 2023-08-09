from scv.job_parser import HHCollectingVacancies, SuperJobCollectingVacancies, WorkingWithVacancies, JsonSaveVacancies

def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    HH = HHCollectingVacancies()
    WW = WorkingWithVacancies
    SJV = JsonSaveVacancies()
    SJ = SuperJobCollectingVacancies()
    platforms = ["HeadHunter", "SuperJob"]
    while True:
        SJV.delete_vacancies()
        user_input = input(f'Здравствуйте! Какую будем использовать платформу для поиска вакансий {" or ".join(platforms)}: ')
        if user_input == platforms[0]:
            if user_input == platforms[0]:
                search_query = input(f"Искать будем на платформе: {platforms[0]}. Введите поисковый запрос: ")
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                if top_n > 100:
                    print("не могу вывести более 100 вакансий =(")
                else:
                    vacancy = HH.search_vacancy(search_query, top_n)
                    SJV.add_json(vacancy)
                    list_vac = WW.hh_vacancy(SJV.get_vacancies())
                    print()
                    print(f"По вашему запросу доступно {len(list_vac)} вакансий")
                    print()
                    input_sort = int(input("""Показать вакансию с большей оплатой, введите: 1.
Отсортировать вакансии по оплате, начиная с большей, введите: 2
Отсортировать вакансии по оплате, начиная с меньшей, введите: 3? """))
                    if input_sort == 1:
                        max_list = max(list_vac)
                        print(max_list)
                    elif input_sort == 3:
                        sorted_up = sorted(list_vac)
                        for vac in sorted_up:
                            print(vac)
                            print()
                    elif input_sort == 2:
                        sorted_down = sorted(list_vac, reverse=True)
                        for vac in sorted_down:
                            print(vac)
                            print()
                    break

        elif user_input == platforms[1]:
            if user_input == platforms[1]:
                search_query = input(f"Искать будем на платформе: {platforms[1]}. Введите поисковый запрос: ")
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                if top_n > 100:
                    print("не могу вывести более 100 вакансий =(")
                else:
                    vacancy = SJ.search_vacancy(search_query, top_n)
                    SJV.add_json(vacancy)
                    list_vac = WW.sj_vacancy(SJV.get_vacancies(), top_n)
                    print()
                    print(f"По вашему запросу доступно {len(list_vac)} вакансий:")
                    print()
                    input_sort = int(input("""Показать вакансию с большей оплатой, введите: 1.
Отсортировать вакансии по оплате, начиная с большей, введите: 2
Отсортировать вакансии по оплате, начиная с меньшей, введите: 3? """))
                    if input_sort == 1:
                        max_list = max(list_vac)
                        print(max_list)
                    elif input_sort == 3:
                        sorted_up = sorted(list_vac)
                        for vac in sorted_up:
                            print(vac)
                            print()
                    elif input_sort == 2:
                        sorted_down = sorted(list_vac, reverse=True)
                        for vac in sorted_down:
                            print(vac)
                            print()
                    break

if __name__ == "__main__":
    user_interaction()