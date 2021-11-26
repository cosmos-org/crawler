import pickle

import requests
from bs4 import BeautifulSoup

data = []
url = 'https://tinhte.vn/thread/tren-tay-macbook-pro-16-m1-max-khong-dep-nhung-rat-ngon.3427519'
r = requests.get(url, headers={'User'
                               '-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) '
                                         'Gecko/20030624 Netscape/7.1 (ax)'})
soup = BeautifulSoup(r.text, 'html.parser')
x1 = soup.find_all('span', class_='xf-body-paragraph')
for i in x1:
    print(i.get_text())
# x2 = soup.find_all('div', id='post-61279911').get_text()
# print(x2)
