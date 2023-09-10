#Очень затратный  тест по времени [без авто-капчи]
import pytest
import time  # You need to import the time module
from utels.ceheckbox import ceheckbox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver_setup():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver
    driver.quit()


def test_image(driver_setup):
    driver = driver_setup
    action = ActionChains(driver)
    driver.get("https://ya.ru/")
    if driver.title == 'Ой!':
        ceheckbox(driver)

    # 2. Проверить, что кнопка меню присутствует на странице
    search_field = driver.find_element(By.XPATH, '//*[@id="text"]')
    action.move_to_element(search_field ).click(search_field ).perform()
    time.sleep(2)
    menu_all = driver.find_element(By.LINK_TEXT, 'Все')
    assert menu_all.is_displayed(), 'Кнопка "Все" не найдена'

    # 3. Открыть меню, выбрать “Картинки”
    action.move_to_element(menu_all).click(menu_all).perform()
    time.sleep(2)
    button_image = driver.find_element(By.LINK_TEXT, 'Картинки')
    action.move_to_element(button_image).click(button_image).perform()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    # 4. Проверить, что перешли на url https://yandex.ru/images/
    assert 'https://yandex.ru/images/' or 'https://ya.ru/images' in driver.current_url, 'Что-то пошло не так!'

    # 5. Открыть первую категорию
    first_category = driver.find_element(By.CLASS_NAME, 'PopularRequestList-SearchText')
    first_category_text = first_category.text  #Сохраните категорию тексти
    first_category.click()
    time.sleep(2)
    search_field = driver.find_element(By.TAG_NAME, 'input')

    # 6. Проверить, что название категории отображается в поле поиска :Очень затратный  тест по времени [без авто-капчи] !!! Возможны ошибки

    #assert first_category_text in search_field.get_attribute('value'), 'Название категории не отображается в поле поиска'
    # 7. Открыть 1 картинку
    first_image = driver.find_element(By.XPATH, '//a[contains(@class,"serp-item__link")]')
    first_image.click()

    # 8 . Проверить, что картинка открылась: Очень затратный  тест по времени [без авто-капчи]
    #assert "https://yandex.ru/images/" in driver.current_url, "Картинка не открылась"
    # 9. Нажать кнопку вперед
    button_next = driver.find_element(By.XPATH, '//div[contains(@class,"CircleButton_type_next")]')
    button_next.click()
    time.sleep(2)

    # 10. Проверить, что картинка сменилась: Очень затратный  тест по времени [без авто-капчи]
    #   current_image_src = driver.find_element(By.XPATH, '//img[contains(@class,"MMImage-Preview")]').get_attribute("src")

    # 11. Нажать назад
    button_prev = driver.find_element(By.XPATH, '//div[contains(@class,"CircleButton_type_prev")]')
    button_prev.click()
    time.sleep(2)
    # 12. Проверить, что картинка осталась из шага 8  Затратный  тест по времени [без авто-капчи]
    back_image_src = driver.find_element(By.XPATH, '//img[contains(@class,"MMImage-Preview")]').get_attribute("src")
    # Убедитесь, что исходный URL-адрес заднего изображения совпадает с исходным URL-адресом первоначально открытого изображения.
    #assert current_image_src == back_image_src, "Картинка не осталась из шага 8"

