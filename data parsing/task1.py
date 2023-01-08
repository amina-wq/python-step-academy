#1.	Реализуйте код, который загружает данные с сайта https://jsonplaceholder.typicode.com/todos/1/
# и записывает это в json файл.

import requests
import json
import time
from threading import Thread
import multiprocessing
import asyncio
import aiohttp 

def download(file_postfix: str) -> None:
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{file_postfix + 1}/')
    with open(f'data/file_{file_postfix}.json', 'w') as opened_file:
        json.dump(response.json(), opened_file)

def sync_download():
    start = time.perf_counter()
    for i in range(50):
        download(i)
    end = time.perf_counter()
    print(f'Время выполнения последовательно: {end-start}') 

def thread_download():
    start = time.perf_counter()
    for i in range(50):
        th = Thread(target=download, args=(i, ))
        th.start()
    end = time.perf_counter()
    print(f'Время выполнения многопоточно: {end-start}')


def multi_download():
    start = time.perf_counter()
    for i in range(50):
        p = multiprocessing.Process(target=download, args=(i, ))
        p.start()
    end = time.perf_counter()
    print(f'Время выполнения мультипроцессорно: {end-start}')

async def download_2(file_postfix: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url= f'https://jsonplaceholder.typicode.com/todos/{file_postfix + 1}/') as response_obj:
            data = await response_obj.json()
            with open(f'data/file_{file_postfix}.json', 'w') as opened_file:
                json.dump(data, opened_file)


def async_download():
    start = time.perf_counter()
    async def start_a():
        return await asyncio.gather(*[download_2(i) for i in range(50)])
    asyncio.run(start_a())
    end = time.perf_counter()
    print(f'Время выполнения асинхрoнно: {end-start}')


if __name__ == '__main__':
    sync_download()
    thread_download()
    multi_download()
    async_download()