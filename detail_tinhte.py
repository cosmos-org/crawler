import pickle

import requests
from bs4 import BeautifulSoup
data = []
with open('list_href_tinhte.pkl', 'rb') as f:
    x = pickle.load(f)
for url in x:
    r = requests.get(url, headers={'User'
                                   '-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) '
                                             'Gecko/20030624 Netscape/7.1 (ax)'})
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        x1 = soup.find('span', class_='xf-body-paragraph').get_text()
        data.append(x1)
    except:
        print("An exception occurred")
    data.append(x1)
with open('data_tinhte.pkl', 'wb') as f:
    pickle.dump(data, f)
