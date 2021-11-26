import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pickle

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

NUMBER_CLICK_MORE_DATA = 10
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver.exe")
url = "https://cellphones.com.vn/sforum/"
driver.get(url)
time.sleep(1)
for i in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
for i in range(NUMBER_CLICK_MORE_DATA):
    driver.find_element('div.jeg_block_loadmore>a').click()
    time.sleep(random.randint(5, 10))
elements = driver.find_elements("body > div.jeg_viewport > div.elementor.elementor-56052 > div > div "
                                "> "
                                "section.elementor-section.elementor-top-section.elementor-element"
                                ".elementor-element-cad13ec.elementor-section-full_width.elementor"
                                "-section-height-default.elementor-section-height-default > div > div "
                                "> div > div > div > div > div > div > div > div > "
                                "section.elementor-section.elementor-top-section.elementor-element"
                                ".elementor-element-43001d1f.elementor-section-full_width.elementor"
                                "-hidden-desktop.elementor-section-height-default.elementor-section"
                                "-height-default > div > div > div > div > div > "
                                "div.elementor-element.elementor-element-108f5e8a.elementor-widget"
                                ".elementor-widget-jnews_block_3_elementor > div > div > "
                                "div.jeg_posts.jeg_block_container > div.jeg_posts.jeg_load_more_flag "
                                "> article > div.jeg_postblock_content > h3 >a")
href = [ele.get_attribute("href") for ele in elements]
print(href)
with open('list_href_cellphones.pkl', 'wb') as f:
    pickle.dump(href, f)
driver.quit()
