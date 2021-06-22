#!/usr/bin/python3
import requests
import datetime
#import asyncio
#import aiohttp
import colorama #colored print
colorama.init(autoreset=True)
url= 'https://loremflickr.com/320/240'


CATS_COUNT= 50
start_time = datetime.datetime.now()

def download(url, session, cat_number):
  res= session.get(url,allow_redirects=True)
  data= res.content
  print(f'Кот номер: {cat_number} загружен')
  save(data, str(res.url))


def save(page, url):
  name=url.split('/')[-1]
  with open(name, 'wb') as f:
    f.write(page)


def main():
  session=requests.session()
  for cat_number in range(CATS_COUNT):
    download(url, session, cat_number)

print(colorama.Fore.GREEN+f'Загружаю {CATS_COUNT} котов')

main()

diff_time = datetime.datetime.now() - start_time
print(diff_time)
