from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  brower import  ceheckbox
import time

def go_to_images(driver):
    parameters = dict()
    element = driver.find_element(By.XPATH, '//*[@id="text"]')
    action.move_to_element(element).click(element).perform()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT, 'Все')
    parameters['button_all'] = element.is_displayed()
    action.move_to_element(element).click(element).perform()
    time.sleep(1)
    element = driver.find_element(By.LINK_TEXT, 'Картинки')
    action.move_to_element(element).click(element).perform()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    parameters['url_task2'] = driver.current_url
    time.sleep(1)
    first_link = driver.find_elements(By.CLASS_NAME, 'PopularRequestList-SearchText')
    first_link[0].click()
    time.sleep(1)
    element = driver.find_element(By.XPATH, '//a[contains(@class,"serp-item__link")]')
    element.click()
    parameters['url_image_1'] = driver.current_url
    time.sleep(1)
    element = driver.find_element(By.XPATH, '//div[contains(@class,"CircleButton_type_next")]')
    element.click()
    time.sleep(1)
    parameters['url_image_2'] = driver.current_url
    element = driver.find_element(By.XPATH, '//div[contains(@class,"CircleButton_type_prev")]')
    element.click()
    time.sleep(1)
    parameters['url_image_test'] = driver.current_url
    return parameters



# инициализация

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)
url = 'https://ya.ru/'


#открывает сайт
driver.get(url)
if driver.title == 'Ой!':
    ceheckbox(driver)
parameters = go_to_images(driver)

for i,j in parameters.items():
    print(i,j)

time.sleep(15)





