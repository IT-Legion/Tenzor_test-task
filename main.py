from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains

def run(driver, action):
    main_page = MainPage(driver, action)
    main_page.open_url("https://ya.ru/")
    main_page.run_script()

# инициализация
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)
run(driver, action)


