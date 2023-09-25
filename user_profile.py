from base_page import BasePage, EC
from selenium.webdriver.common.action_chains import ActionChains
from links import Links
from random import randint

class UserProfile(BasePage):

    TARGET_JOB_NUMBER = 0
    AMOUNT_CONTENT = ('xpath', '(//div[contains(@class, "Cover-content-yv3")])')


    def go_too_content_page(self):
        """Логика выбора контента у автора. Если переменная TARGET_JOB_NUMBER == 0 > рандомный выбор элемента.
        Иначе, будет использоваться номер совпадения например: TARGET_JOB_NUMBER == 1
        """

        # переключение на новое окно
        self.swith_too_new_window(self.AMOUNT_CONTENT)

        # проверка отображения первой иконки проекта
        AMOUNT = ('xpath', '(//div[@class="Cover-content-yv3"])')
        content_page = self.chrome_driver.find_elements('xpath', '(//div[@class="Cover-content-yv3"])')
        amount_page = len(content_page) # количество проектов


        if self.TARGET_JOB_NUMBER == 0:
            random_count = randint(1, amount_page)
            random_locator = ('xpath', f'({self.AMOUNT_CONTENT[1]})[{random_count}]') # формируем локатор
            CONTENT = self.find_visibility_of_element(random_locator, 'Список работ не прогрузился')
            ActionChains(self.chrome_driver).move_to_element(CONTENT).click(CONTENT).perform()
            print(f'Случайный выбор работы > № {amount_page}')

        else:
            nuber_locator = ('xpath', f'({self.AMOUNT_CONTENT[1]})[{self.TARGET_JOB_NUMBER}]')
            CONTENT = self.find_visibility_of_element(nuber_locator, 'элемент не кликабельный')
            ActionChains(self.chrome_driver).move_to_element(CONTENT).click(CONTENT).perform()
            print(f'Была указана работа > № {self.TARGET_JOB_NUMBER}')
            print()

            print(self.AMOUNT_CONTENT[1])







