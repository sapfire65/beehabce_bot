import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import uniform
from links import Links
import re

class BasePage:
    URL_IP_API = 'http://ip-api.com/line'

    START_URL_BEHANCE = Links.START_URL
    LOGO_ADOBE = ('xpath', '//div[@class="PrimaryNav-adobeLogo-VeZ"]')


    def __init__(self, chrome_driver):
        self.chrome_driver = chrome_driver
        self.wait = WebDriverWait(chrome_driver, 15, 1)


    def open_behance(self):
        self.chrome_driver.get(self.START_URL_BEHANCE)
        self.chrome_driver.stop_client()
        self.chrome_driver.refresh()
        print(f'Страница открыта')
        sleep(5)

    def is_opened(self):
        # Проверяем что логотип загрузился и отображается. Значит страница загружена
        self.wait.until(EC.visibility_of_element_located(self.LOGO_ADOBE))



    def check_ip(self):
        self_ip = requests.get(self.URL_IP_API).text
        self_ip = str(self_ip)
        text = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', self_ip)
        text = str(text[0])
        print(f'\nIP: {text}\n')
        return text


    def find_visibility_of_element(self, locator, exeptions_text ='Елемент не отображается'):
        """Поиск видимого элемента на странице

        :param locator: (str) локатор
        :param exeptions_text: (str) текст исключения
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element

        except TimeoutException:
            print(exeptions_text)
            self.error_info()

    def find_element_to_be_clickable(self, locator, exeptions_text ='Елемент не кликабелен'):
        """Поиск кликабельного элемента на странице

        :param locator: (str) локатор
        :param exeptions_text: (str) текст исключения
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            return element

        except TimeoutException:
            print(exeptions_text)
            self.error_info()

    def error_info(self, exception_text = 'Смотреть скрин ошибки'):
        """Вспомогательный метод.
        Выводит дату / время / сообщение исключения функции
        Делает скриншот в папку - screen

        :exception_text - принимает str / сообщение исключения
        """
        file_name = exception_text
        self.chrome_driver.get_screenshot_as_file(f'screen/{file_name}.png')
        self.chrome_driver.quit()


    def send_keys_random_speed(self, locator_input, my_text):
        """Вводит текст с рандомными паузами как человек

        :param locator_input: (str) - locator for element
        :param my_text: (str) - текст запроса
        """
        my_input = self.find_visibility_of_element((locator_input))
        my_input.click()
        letters = list(my_text)

        for i in range(len(my_text)):
            random_count = uniform(0, 0.4) # Рандомное число с плавающей точкой
            my_input.send_keys(letters[i])
            sleep(random_count)
        sleep(1)


    def swith_too_new_window(self, selector, exception_text='Ошибка перехода на новую вкладку'):
        """
        Функция проверяет достоверность наличия двух открытых вкладок.
        И если это так, активирует последнюю открытую вкладку.
        Проверяет отображение уникального контрольного обьекта.
        Возвращает проверяемый объект.

        :param exception_text:(str) / Текст оповещения - в случае если ключевой объект не виден.
        :param selector:(str) / например ('xpath', selector)
        """

        count_window = self.chrome_driver.window_handles
        if len(count_window) == 2:
            last_window = count_window[1]
            self.chrome_driver.switch_to.window(last_window)
            print('Переключение на новое окно')

        self.find_visibility_of_element(selector, exception_text)
        return selector







