import requests
import os
import random
from bs4 import BeautifulSoup
os.chdir(os.getcwd())
x = requests.get('https://icore.kz/resheniya/')
y=x.text
soup = BeautifulSoup(x.text, 'html.parser')
items = soup.findAll('img')
img_urls=[]
for i in range(len(items)):
    url = items[i]["src"]
    img_urls.append(url)


for i in range(10):
    rand_url=img_urls[random.randint(0,len(img_urls)-1)]
    r = requests.get(f"{rand_url}")
    os.mkdir(f"img{i}")
    with open(f"img{i}/img{i}.jpg", 'bw') as f:
        f.write(r.content)