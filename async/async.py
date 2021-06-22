#!/usr/bin/python3

#from requests import get, session
import datetime
import asyncio
import aiohttp
import colorama #colored print
colorama.init(autoreset=True)
url= 'https://loremflickr.com/320/240'
#s=session()

CATS_COUNT= 50
start_time = datetime.datetime.now()

async def download(url, session, cat_number):
  res=await session.get(url,allow_redirects=True)
  data= await res.read()
  print(f'Кот номер: {cat_number} загружен')
  save(data, str(res.url))


def save(page, url):
  name=url.split('/')[-1]
  with open(name, 'wb') as f:
    f.write(page)

async def main():
  tasks=[]
  async with aiohttp.ClientSession() as session:
    for cat_number in range(CATS_COUNT):
      task=asyncio.create_task(download(url, session, cat_number))
      tasks.append(task)
    await asyncio.gather(*tasks)

print(colorama.Fore.GREEN+f'Загружаю {CATS_COUNT} котов')
asyncio.run(main())

diff_time = datetime.datetime.now() - start_time
print(diff_time)
