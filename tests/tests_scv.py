from scv.job_parser import HHCollectingVacancies, SuperJobCollectingVacancies, WorkingWithVacancies, JsonSaveVacancies

def test_SuperJobCollectingVacancies_search_vacancy():
    SJ = SuperJobCollectingVacancies()
    vac = SJ.search_vacancy("pyasd", 2)
    assert vac == {'error': {'code': 400,
           'error': 'app_key_required',
           'message': 'Необходимо передать ключ приложения. Зарегистрироваться '
                      'можно по адресу https://api.superjob.ru/register/'}}

def test_WorkingWithVacancies_hh_vacancy(fixture_ww_hh, fixture_test_WW_search_hh):
    WW = WorkingWithVacancies
    vac = WW.hh_vacancy(fixture_ww_hh)
    vac1 = WW.hh_vacancy(fixture_test_WW_search_hh)
    assert vac == None
    assert len(vac1) == 2

def test_WW_sj_vacancy(fixture_ww_sj_list, fixture_ww_sj):
    WW = WorkingWithVacancies
    vac = WW.sj_vacancy(fixture_ww_sj_list, 1)
    vac1 = WW.sj_vacancy(fixture_ww_sj, 1)
    assert vac == None
    assert len(vac1) == 1

def test_WorkingWithVacancies_add():
    WW1 = WorkingWithVacancies('','','', 2)
    WW2 = WorkingWithVacancies('','','', 23)
    WW3 = WorkingWithVacancies('','','', 20)
    WW4 = WorkingWithVacancies('', '', '', 20)
    assert WW1 + WW2 == 25
    assert WW1 - WW2 == -21
    assert WW1 < WW2
    assert WW1 <= WW2
    assert WW3 > WW1
    assert WW3 >= WW1
    assert WW3 <= WW4
    assert WW3 >= WW4


def test_SaveVacancies(fixture_test_search_vacancy_hh):
    JSV = JsonSaveVacancies()
    JSV.add_json(fixture_test_search_vacancy_hh)
    vac = JSV.get_vacancies()
    assert vac == [fixture_test_search_vacancy_hh]

def test_SaveVacancies_delet(fixture_test_search_vacancy_hh):
    JSV = JsonSaveVacancies()
    JSV.add_json(fixture_test_search_vacancy_hh)
    vac = JSV.delete_vacancies()
    assert vac == None





