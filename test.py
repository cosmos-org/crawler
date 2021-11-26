import requests
from bs4 import BeautifulSoup

url = 'https://mbasic.facebook.com/groups/mecongnghe/'
r = requests.get(url, headers={'User'
                               '-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) '
                                         'Gecko/20030624 Netscape/7.1 (ax)'})
print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
x1 = soup.find_all('div', role='article')
for i in x1:
    print(i)
