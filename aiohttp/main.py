import aiohttp
import asyncio
import random
from bs4 import BeautifulSoup
import os
os.chdir(os.getcwd())
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://icore.kz/resheniya/') as response:
            return await response.text()
async def second(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()
y = asyncio.run(main())
soup = BeautifulSoup(asyncio.run(main()), 'html.parser')
items = soup.findAll('img')

img_urls=[]
for i in range(len(items)):
    url = items[i]["src"]
    img_urls.append(url)

for i in range(10):
    rand_url=img_urls[random.randint(0,len(img_urls)-1)]
    r = asyncio.run(second(rand_url))
    os.mkdir(f"img{i}")
    with open(f"img{i}/img{i}.jpg", 'bw') as f:
        f.write(r)