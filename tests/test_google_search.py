#Часа 1.5-2ч заняло по сравнению с 70ч часов мечения  на Е"№!6 ЯНДЕКСЕ!
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver_setup():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_google_search(driver_setup):
    # 1. Зайти на https://www.google.com/
    driver = driver_setup
    driver.get("https://www.google.ru/")
    time.sleep(2)
    # 2. Проверить наличие поля поиска
    search_box = driver.find_element(By.TAG_NAME, 'textarea')
    assert search_box.is_displayed(), "Поле поиска не найдено на странице Google"
    # 3. Ввести в поиск "Тензор"
    search_box.send_keys("Тензор")
    time.sleep(2)
    # 4. Проверить, что появилась таблица с подсказками (suggest)
    suggest_list = driver.find_element(By.CSS_SELECTOR, "#Alh6id > div.erkvQe > div > ul")
    assert suggest_list.is_displayed(), "Таблица с подсказками не появилась"
    # 5. Нажать Enter
    search_box.submit()
    time.sleep(2)
    # 6. Проверить, что появилась страница результатов поиска
    wait = WebDriverWait(driver, 30)
    search_results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "yuRUbf")))
    # Вывод найденных результатов
    assert len(search_results) > 0, "Страница результатов поиска не загрузилась"
    # 7. Проверить, что первая ссылка ведет на сайт tensor.ru
    assert "tensor.ru" in str(search_results[0].text), "Первая ссылка не ведет на tensor.ru"
