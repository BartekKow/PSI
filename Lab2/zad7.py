import aiohttp
import asyncio

async def fetch(url, name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            with open(name, 'wb') as f:
                f.write(content)

async def main() -> None:
    await fetch("https://pbs.twimg.com/profile_images/1055686976798670848/jA-Yn1Hh_400x400.jpg", "img.png")

if __name__ == "__main__":
    asyncio.run(main())
