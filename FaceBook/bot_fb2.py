import time
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from selenium.webdriver.common.by import By


def random_sleep(mins=1, maxs=5):
    sleep(randint(mins, maxs))


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

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options
                          )
driver.get('https://mbasic.facebook.com/')
username = 'duong.fbk02@gmail.com'
password = 'd12345678@'
username_ele = driver.find_element(By.NAME, 'email')
username_ele.send_keys(username)
random_sleep(1, 5)
password_ele = driver.find_element(By.NAME, 'pass')
password_ele.send_keys(password)
random_sleep(1, 5)
login_ele = driver.find_element(By.NAME, 'login')
random_sleep(1, 5)
login_ele.click()
random_sleep(1, 5)
driver.get('https://mbasic.facebook.com/groups/mecongnghe/permalink/791360844965685/?refid=18&_ft_=qid'
           '.-7389833590087587916%3Amf_story_key.791360844965685%3Atop_level_post_id.791360844965685%3Atl_objid'
           '.791360844965685%3Acontent_owner_id_new.100028747620128%3Apage_id.479808602787579%3Asrc.22'
           '%3Astory_location.6%3Astory_attachment_style.photo%3Afilter.GroupStoriesByActivityEntQuery%3Aott'
           '.AX8Lb4T5xgDiSh0B%3Atds_flgs.3&__tn__=%2AW-R#footer_action_list')

ele_content = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/footer/div[1]/abbr")
print(ele_content.text)

