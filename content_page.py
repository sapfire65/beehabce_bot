from base_page import BasePage, EC
from selenium.webdriver.common.action_chains import ActionChains
from links import Links


class ContentPage(BasePage):

    ICON_LIKE = ('xpath', '//div[@class="Project-appreciateWithPulsePoint-P5b"]')
    LIKET_IT = '//div[@source="projectContentSidebar"]/div[@data-adobe-analytics="UnappreciateClick"]'

    def click_like(self):
        # проверка на кликабельность кнопки лайк
        icon_like = self.find_element_to_be_clickable(self.ICON_LIKE, 'Кнопка ЛАЙК не кликабельна')
        try:
            status_like = ''
            status_like = self.chrome_driver.find_element('xpath', self.LIKET_IT).get_attribute('data-adobe-analytics')
        except: ...

        if not status_like == 'UnappreciateClick':
            icon_like.click()
            print('Лайк поставлен')
        else:
            print('Лайк был поставлен ранее')

    def intoli_com(self):

        elem_1 = self.chrome_driver.find_element('xpath', '(//span[@class="age"])[1]').text
        elem_2 = self.chrome_driver.find_element('xpath', '(//span[@class="age"])[2]').text
        elem_3 = self.chrome_driver.find_element('xpath', '(//span[@class="age"])[3]').text
        elem_4 = self.chrome_driver.find_element('xpath', '(//span[@class="age"])[4]').text
        elem_5 = self.chrome_driver.find_element('xpath', '(//span[@class="age"])[5]').text
        elem_6 = self.chrome_driver.find_element('xpath', '(//span[@class="age"])[6]').text

        print(f'{elem_1} | {elem_2} | {elem_3} | {elem_4} | {elem_5} | {elem_6}')







