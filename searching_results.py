from base_page import BasePage, EC
from links import Links
from selenium.webdriver.common.action_chains import ActionChains

class SerchResults(BasePage):

    BANNER = ('xpath', '//div[@class="Users-bannerWrapper-ERm"]')
    USER_CARD = ('xpath', '(//div[@class="UserSummary-ownerLinkWrap-OlV"])[1]')

    def check_and_click_user_card(self):
        """Проверят отображение уникального элемента страницы (банера) и кликает на карточку нужного юзера"""
        self.find_visibility_of_element(self.BANNER, 'Проверочный элемент (баннер) - не загрузился')
        user =  self.find_element_to_be_clickable(self.USER_CARD, 'Карточка юзера не кликабельна')
        ActionChains(self.chrome_driver).move_to_element(user).click(user).perform()
        print('Клик по карточке юзера')

