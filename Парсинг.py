import requests
from bs4 import BeautifulSoup
import re

url = 'https://vladivostok.drom.ru/toyota/page'

car_link = []
car_name = []
car_price = []
car_town = []
car_har = []
all = []
urls = []

for page in range(1, 16):
    req = requests.get(url + str(page))
    text = req.text
    soup = BeautifulSoup(text, "lxml")

    for t in soup.find_all('a', {'class': 'css-xb5nz8 e1huvdhj1'}):
        car_link.append(t.get('href'))

    for d in soup.find_all('span', {'data-ftid': 'bull_title'}):
        car_name.append(d.text)

    for x in soup.find_all('span', {'class': 'css-46itwz e162wx9x0'}):
        car_price.append(re.sub(r'[^\d,.]', '', x.text))

    for z in soup.find_all('div', {'class': 'css-1x4jcds eotelyr0'}):
        for town in z.find_all('span'):
            car_town.append(town.text)

    for v in soup.find_all('div', {'class': 'css-1fe6w6s e162wx9x0'}):
        car_har.append(v.text)

for k in range(len(car_name)):
    all.append([car_name[k], car_link[k], car_price[k], car_town[k], car_har[k]])

for g in all:
    if g[0][:13] == 'Toyota Probox':
        print(g)



