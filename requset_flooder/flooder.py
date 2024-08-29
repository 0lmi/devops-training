import aiohttp
import asyncio
import time
import logging
import os

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S.%f',
)

logger = logging.getLogger(__name__)

async def make_request(session, url, request_number):
    try:
        start_time = time.monotonic()
        async with session.get(url) as response:
            latency = time.monotonic() - start_time
            logger.info(f"Request {request_number + 1}: Status Code: {response.status}, Latency: {latency:.4f} seconds")
    except aiohttp.ClientError as e:
        logger.error(f"Request {request_number + 1}: Failed with error: {e}")

async def make_requests(url, requests_per_second):
    async with aiohttp.ClientSession() as session:
        request_number = 0
        interval = 1 / requests_per_second  # Интервал между запросами в секундах

        while True:
            cycle_start = time.monotonic()

            # Запускаем все запросы для текущего цикла
            tasks = [make_request(session, url, request_number + i) for i in range(requests_per_second)]
            await asyncio.gather(*tasks)

            request_number += requests_per_second

            # Рассчитываем время, затраченное на выполнение запросов
            elapsed_time = time.monotonic() - cycle_start

            # Корректируем задержку на основе затраченного времени
            sleep_time = max(0, 1 - elapsed_time)
            await asyncio.sleep(sleep_time)

# Запуск асинхронной задачи
try:
    asyncio.run(make_requests(url, requests_per_second))
except KeyboardInterrupt:
    logger.info("Execution interrupted by user.")

