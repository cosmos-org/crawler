import time
from datetime import datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
from selenium.webdriver.common.by import By
from pymongo import MongoClient


def random_sleep(mins=1, maxs=5):
    sleep(randint(mins, maxs))


def normalize_text(text):
    return text


class BotTinhte:
    def __init__(self):
        client = MongoClient('mongodb+srv://duongdt:duongdt123@demo.pe29x.mongodb.net')
        mydb = client['cosmos']
        self.mycol = mydb['opinions']
        self.NUMBER_CLICK_MORE_DATA = 500
        PROXY = 'http://127.0.0.1:8118'
        self.list_url_post = []
        self.list_post = []
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
        chrome_options.add_argument('--proxy-server=%s' % PROXY)

        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                                       options=chrome_options,
                                       )
        self.driver.get("https://tinhte.vn/")

    def parse(self):
        for i in range(self.NUMBER_CLICK_MORE_DATA):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            random_sleep()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "li.jsx-934348644>div>article>a:nth-child(1)")
        self.list_url_post = [ele.get_attribute("href") for ele in elements]

    def save_list_url(self):
        textfile = open("/home/duong/Project/Python/crawler/TinhTe/post_url.txt", "w")
        for url in self.list_url_post:
            textfile.write(str(url) + "\n")
        textfile.close()

    def close(self):
        self.driver.close()

    def crawl_post_content(self, post_url):
        post = {}
        random_sleep()
        self.driver.get(post_url)
        ele_content = self.driver.find_element(By.XPATH, "//article")
        post['url'] = post_url
        post['content'] = ele_content.text
        ele_author = self.driver.find_element(By.XPATH, "//div[contains(@class, 'author-name')]/a")
        post['author'] = ele_author.text
        post['url_author'] = ele_author.get_attribute('href')
        ele_date = self.driver.find_element(By.XPATH, "//span[contains(@class, 'date')]")
        post['created_time'] = ele_date.text
        ele_comment = self.driver.find_element(By.XPATH, "//span[contains(@class, 'comment')]")
        post['comment_number'] = ele_comment.text
        try:
            ele_rating = self.driver.find_element(By.XPATH, "//div[contains(@class, 'total-reactions')]")
            post['rating'] = ele_rating.text
        except:
            post['rating'] = '0'
        post['crawled_time'] = datetime.utcnow()
        post['type'] = 'post'
        post['source'] = 'Tinh Te'
        self.mycol.insert_one(post)


if __name__ == '__main__':
    a = BotTinhte()
    a.parse()
    for i in a.list_url_post:
        try:
            a.crawl_post_content(i)
        except:
            print("Loi")
    a.close()
