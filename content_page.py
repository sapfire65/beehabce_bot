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









