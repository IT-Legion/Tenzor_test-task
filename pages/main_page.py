from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import  time


class MainPage(BasePage):
    SEARCH_STRING = (By.XPATH, '//*[@id="text"]')
    MENU_ALL = (By.LINK_TEXT, 'Все')
    IMAGES_OPTION = (By.LINK_TEXT, 'Картинки')
    FIRST_CATEGORY = (By.CLASS_NAME, 'PopularRequestList-SearchText')
    FIRST_IMAGE = (By.XPATH, '//a[contains(@class,"serp-item__link")]')
    BUTTON_NEXT = (By.XPATH, '//div[contains(@class,"CircleButton_type_next")]')
    BUTTON_PREV = (By.XPATH, '//div[contains(@class,"CircleButton_type_prev")]')
    LINK_LIST = (By.CSS_SELECTOR, ".organic__url-text")
    search_object = 'Тензор'

    def first_image(self):
        """Для контроля логики  нового окна."""
        self.find_window(1)
        self.click_through_elements(*self.FIRST_CATEGORY)
        self.click_through_elements(*self.FIRST_IMAGE)
        self.click_element(*self.BUTTON_NEXT)
        self.click_element(*self.BUTTON_PREV)



    def activate_search_string (self):
        '''
        Активирует поисковую строку.
        :return:
        '''
        self.click_element(*self.SEARCH_STRING)

    def run_picture_script(self):
        """
        Запускает скрипт
        :return:
        """
        self.activate_search_string()
        self.move_to_element_and_click(*self.MENU_ALL)
        self.click_element(*self.IMAGES_OPTION)
        self.first_image()
        self.find_window()

        #self.activate_search_string()

        #self.send_keys()


    def get_link_list(self):
        return self.find_element(*self,__LINK_LIST)

    def send_keys(self):
        return send_keys(self.search_object)













