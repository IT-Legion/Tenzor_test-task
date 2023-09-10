import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utels.ceheckbox import ceheckbox

@pytest.fixture
def driver_setup():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_search_scenario(driver_setup):
    driver = driver_setup

    # Переход на страницу
    driver.get("https://ya.ru/")
    if driver.title == 'Ой!':
        ceheckbox(driver)

    # Проверка наличия поля поиска
    search_field = driver.find_element(By.XPATH, '//*[@id="text"]')
    assert search_field.is_displayed(), "Поле поиска не найдено."

    # Ввод "Тензор" в поле поиска
    search_field.send_keys("Тензор")

    # Проверка, что появилась таблица с подсказками (suggest)
    suggest_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".mini-suggest__popup"))
    )
    assert suggest_table.is_displayed(), "Таблица с подсказками не найдена."

    # Нажатие клавиши Enter
    search_field.submit()

    # Проверка, что появилась страница результатов поиска
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(((By.CSS_SELECTOR, ".organic__url-text")))
    )
    assert len(search_results) > 0, "Страница результатов поиска не найдена."
    # Проверка, что первая ссылка ведет на сайт tensor.ru
    search_results[0].click()
    driver.switch_to.window(driver.window_handles[1])
    assert "tensor.ru" in driver.current_url, "Первая ссылка не ведет на сайт tensor.ru."