from loguru import logger
import asyncio, random, webbrowser

async def main() -> None:
	n = random.randint(1, 10)
	url = 'https://google.com'

	browser = webbrowser.get()

	logger.debug(f'{n} opennings.')
	for i in range(n):
		browser.open_new(url)
		await asyncio.sleep(1)

if __name__ == '__main__':
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.run_until_complete(main())
	loop.close()

	