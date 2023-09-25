from base_page import BasePage, EC
from selenium.webdriver.common.keys import Keys
from links import Links

class StartPage(BasePage):
    SEARCH_TEXT = 'Iylia Cherenkova'
    SEARCH_INPUT = ('xpath', '//input[@name="search"]')
    BUTTON_PIPLE = ('xpath', '//a[@href="/search/users"]')


    def click_button_piple(self):
        button = self.find_element_to_be_clickable(self.BUTTON_PIPLE)
        button.click()

        print('Нажали на кнопку - Люди')


    def enter_text_into_search(self):
        """Вводит в поисковик запрос и нажимает клавишу ENTER"""
        elem = self.find_element_to_be_clickable(self.SEARCH_INPUT)
        self.send_keys_random_speed(self.SEARCH_INPUT, self.SEARCH_TEXT)
        elem.send_keys(Keys.ENTER)
        print('Текст запроса введен, нажат ENTER')

        