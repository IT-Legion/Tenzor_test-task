from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  brower import  ceheckbox
import  os


def get_url(driver):
    '''
     Производит поиск и открывает 1 страницу
    :return: Словарь для теста
    '''
    parameters = dict()
    search_string = driver.find_element(By.XPATH, '//*[@id="text"]')
    #Отправить в тест
    parameters['search_string'] = search_string.is_displayed()
    search_string.send_keys('Тензор')
    # Найти таблицу

    search_string.submit()
    search_results = driver.find_elements(By.CSS_SELECTOR, ".organic__url-text")
    search_results[0].click()
    driver.switch_to.window(driver.window_handles[1])
    parameters['url_task1'] = driver.current_url
    driver.close()
    return parameters

# инициализация
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = 'https://ya.ru'

#открывает сайт
driver.get(url)
if driver.title == 'Ой!':
    ceheckbox(driver)


parameters = get_url(driver)
for i,j in parameters.items():
    print(i,j)







