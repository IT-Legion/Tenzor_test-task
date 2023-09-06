import pytest
from task_2 import  parameters


def test_search_string():
    pass
    #assert parameters['search_string'] == True,'Поисковая строка не найдена'

def test_button_all():
    assert parameters['button_all'] == True


def test_url():
    if parameters['url_task2'] == 'https://yandex.ru/images/':
        print('Ссылка: Корректна')
    else:
        print('Ссылка: Некорректна')

def test_picture_change():
    assert parameters['url_image_1'] != parameters['url_image_2'],'Картинка не переключилась'

def test_back_picture():
    assert parameters['url_image_1'] == parameters['url_image_test'],'Картинка не вернулась'

