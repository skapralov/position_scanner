import asyncio
from pyppeteer import launch
import pyppeteer


URL = {'google': '', 'yandex': ''}
pyppeteer.DEBUG = True


async def main(ports=(9050, 9051)):
    browser = await launch(args=[f'--proxy-server=socks5://127.0.0.1:{ports[0]}', ])
    page = await browser.newPage()
    await page.goto('https://2ip.ru/')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


async def execute_requests_to_google():
    pass


async def execute_requests_to_yandex():
    pass


asyncio.get_event_loop().run_until_complete(main())