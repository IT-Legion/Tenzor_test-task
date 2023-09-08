import time
from utels.ceheckbox import  ceheckbox


data = dict()

class BasePage:


    def __init__(self, driver,action):
        self.driver = driver
        self.action = action


    def open_url(self, url):
        '''
        Открывает сайт.
        '''
        self.driver.get(url)
        time.sleep(1)
        if self.driver.title == 'Ой!':
            ceheckbox(self.driver)
        return  True



    def find_element(self, by, value):
        '''
        Находит элемент.
        '''
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        """
         Находит элементы
        """
        return self.driver.find_elements(by, value)

    def click_element(self, by, value):
        '''
         Производит клик по элементу.
        '''
        element = self.find_element(by, value)
        element.click()
        time.sleep(1)


    def move_to_element_and_click(self, by, value):
        '''
        Наводит и кликает по элементу.
        '''
        element = self.find_element(by, value)
        self.action.move_to_element(element).click(element).perform()
        time.sleep(1)

    def find_window(self,num=0):
        '''
        Переключает окна
        todo: проверку
        '''
        self.driver.switch_to.window(self.driver.window_handles[num])

    def link(self):
        data['step_3'] = self.driver.current_url



















