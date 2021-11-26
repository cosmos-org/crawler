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
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/duong/Project/Python/crawler/chromedriver")
url = "https://tinhte.vn/"
driver.get(url)
time.sleep(random.randint(1, 5))
for i in range(NUMBER_CLICK_MORE_DATA):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randint(1, 5))
elements = driver.find_elements(By.CSS_SELECTOR, "li.jsx-934348644>div>article>a:nth-child(1)")
href = [ele.get_attribute("href") for ele in elements]
print(href)
driver.quit()
