import time
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from selenium.webdriver.common.by import By


def random_sleep(mins=1, maxs=5):
    sleep(randint(mins, maxs))


class bot_fb1:
    def __init__(self):
        CHROMEDRIVER_PATH = '/home/duong/Project/Python/crawler/chromedriver'
        WINDOW_SIZE = "1000,2000"
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--disable-gpu') if os.name == 'nt' else None  # Windows workaround
        chrome_options.add_argument("--verbose")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--ignore-ssl-errors")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--disable-feature=IsolateOrigins,site-per-process")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--ignore-certificate-error-spki-list")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-blink-features=AutomationControllered")
        chrome_options.add_experimental_option('useAutomationExtension', False)
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")  # open Browser in maximized mode
        chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chrome_options.add_argument('disable-infobars')

        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                       options=chrome_options
                                       )
        self.driver.get('https://mbasic.facebook.com/')
        username = 'duong.fbk02@gmail.com'
        password = 'd12345678@'
        username_ele = self.driver.find_element(By.NAME, 'email')
        username_ele.send_keys(username)
        random_sleep(1, 5)
        password_ele = self.driver.find_element(By.NAME, 'pass')
        password_ele.send_keys(password)
        random_sleep(1, 5)
        login_ele = self.driver.find_element(By.NAME, 'login')
        random_sleep(1, 5)
        login_ele.click()
        random_sleep(1, 5)
        self.driver.get('https://mbasic.facebook.com/groups/mecongnghe/')


if __name__ == '__main__':
    
