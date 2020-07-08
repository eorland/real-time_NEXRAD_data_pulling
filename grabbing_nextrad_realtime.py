# -*- coding: utf-8 -*-
from PIL import Image
from bs4 import BeautifulSoup
import requests

url = 'https://radar.weather.gov/ridge/RadarImg/N1P/LWX/'
site = requests.get(url)

soup = BeautifulSoup(site.text, 'html.parser')

images = soup.find_all('a',href=True)

for a in soup.find_all('a', href=True):
    if '.gif' in a['href']:
      img_path = requests.get(url + a["href"])
      print(img_path.content)
      
    with open(str(a['href']), "wb") as f:
        f.write(img_path.content)
        im = Image.open(str(a['href']))
        im.save(str(a['href'])[:-4]+'.png','PNG')


