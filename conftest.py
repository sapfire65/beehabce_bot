import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function', autouse=True)
def chrome_driver(request):
    chrome_options = Options()
    """блок отвечает за отключение обнаружения автоматизации"""
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--incognito')

    """Дополнительные настройки"""
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--homedir=/tmp")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--ignore-certificate-errors-spki-list")
    chrome_options.add_argument('--window-size=1920,1080')

    chrome_options.add_argument("--hide-scrollbars")
    chrome_options.add_argument('--headless')


    chrome_driver = webdriver.Chrome(options=chrome_options)
    request.cls.chrome_driver = chrome_driver
    chrome_driver.delete_all_cookies()

    yield chrome_driver
    chrome_driver.quit()

