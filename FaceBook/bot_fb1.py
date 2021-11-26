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


class bot_fb1:
    def __init__(self):
        client = MongoClient('mongodb+srv://duongdt:duongdt123@demo.pe29x.mongodb.net')
        mydb = client['cosmos']
        self.mycol = mydb['authors']
        self.number_click = 1
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

    def join(self, channel):
        self.driver.get(channel)
        random_sleep()

    def close(self):
        self.driver.close()

    def parse(self):
        list_url = []
        list_c = []
        elements = self.driver.find_elements(By.XPATH, "//article[@class='da dc dm']/footer/div[2]/a[3]")
        elements_c = self.driver.find_elements(By.XPATH, "//article[@class='da dc dm']/footer/div[2]/a[1]")
        for ele in elements:
            list_url.append(ele.get_attribute('href'))
        for ele in elements_c:
            list_c.append(ele.text)
        for i in range(len(list_c)):
            url_post = {'url': list_url[i], 'number_comment': list_c[i]}
            self.list_url_post.append(url_post)

    def load_more_page(self):
        random_sleep()
        self.driver.find_element(By.XPATH, "//div[@id='m_group_stories_container']/div/a").click()

    def save_list_post(self):
        textfile = open("FaceBook/post_url.txt", "w")
        for url in self.list_url_post:
            textfile.write(str(url) + "\n")
        textfile.close()

    def crawl_post_content(self, post_url):
        random_sleep()
        post = {}
        self.driver.get(post_url['url'])
        ele_content = self.driver.find_element(By.XPATH, "//div[@id='m_story_permalink_view']/div[1]/div/div/div[1]")
        post['content'] = ele_content.text
        ele_author = self.driver.find_elements(By.XPATH,
                                               "//div[@id='m_story_permalink_view']/div["
                                               "1]/div/div/header/table/tbody/tr/td[ "
                                               "2]/header//a")
        ele_rating = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[3]")
        ele_created = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/footer/div["
                                                         "1]/abbr")
        post['author'] = ele_author[0].text
        post['url_author'] = ele_author[0].get_attribute('href')
        post['type'] = 'post'
        post['url'] = post_url['url']
        post['source'] = 'Me Cong Nghe - ReLab & Friends'
        post['rating'] = ele_rating.text
        post['comment_number'] = post_url['number_comment']
        post['crawled_time'] = datetime.utcnow()
        post['created_time'] = ele_created.text
        self.list_post.append(post)
        self.mycol.insert(post)


if __name__ == '__main__':
    channel = 'https://mbasic.facebook.com/groups/mecongnghe/'
    a = bot_fb1()
    a.join(channel)
    a.parse()
    for i in range(a.number_click):
        a.load_more_page()
        a.parse()
    print(a.list_url_post)
    for i in a.list_url_post:
        a.crawl_post_content(i)
    a.save_list_post()
    # a.close()
