from selenium.webdriver.common.by import By
import time

def ceheckbox(driver):
    """
    Можно использовать как метод в классе
    :param driver:
    :return:
    """
    element = driver.find_element(By.XPATH, '//*[@id="js-button"]')
    element.click()
    time.sleep(30)

