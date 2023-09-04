from selenium.webdriver.common.by import By
import time

def ceheckbox(driver):
    element = driver.find_element(By.XPATH, '//*[@id="js-button"]')
    element.click()
    time.sleep(30)
