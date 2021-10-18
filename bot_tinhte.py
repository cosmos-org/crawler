import random
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

NUMBER_CLICK_MORE_DATA = 2
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver.exe")
url = "https://tinhte.vn/"
driver.get(url)
time.sleep(1)
for i in range(NUMBER_CLICK_MORE_DATA):
    driver.find_element_by_css_selector('button.jsx-2203663499.load-more-btn').click()
    time.sleep(random.randint(5, 10))
elements = driver.find_elements_by_css_selector("#__next > div.root > div.jsx-4281031340.main-page.home > "
                                                "div.jsx-2790954478.page-layout.false > div > div > "
                                                "div.jsx-2790954478.col-main.additional-padding.undefined > div > "
                                                "div.jsx-3885851162.row > div.jsx-3885851162.col-main > "
                                                "div.jsx-2203663499.latest-threads > div > div > ol > li "
                                                "> div > article > a:nth-child(1)")
href = [ele.get_attribute("href") for ele in elements]
print(href)
with open('list_href_tinhte.pkl', 'wb') as f:
    pickle.dump(href, f)
driver.quit()
