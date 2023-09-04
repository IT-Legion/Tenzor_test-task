from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  brower import  ceheckbox
import time

def get_url(driver):
    search_string = driver.find_element(By.XPATH, '//*[@id="text"]')
    search_string.send_keys('Тензор')
    search_string.submit()
    search_results = driver.find_elements(By.CSS_SELECTOR, ".organic__url-text")
    search_results[0].click()
    driver.switch_to.window(driver.window_handles[1])
    url = driver.current_url
    return url


# инициализация
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = 'https://ya.ru'


#открывает сайт
driver.get(url)
if driver.title == 'Ой!':
    ceheckbox(driver)

first_link = get_url(driver)
print(first_link)







