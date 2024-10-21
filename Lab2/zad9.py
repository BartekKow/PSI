import aiohttp
import asyncio

async def fetch(session, url, retries=3):
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                if 200 <= response.status < 300:
                    return await response.json()
                elif 400 <= response.status < 500:
                    print(f"Client error: {response.status}")
                    return None
                elif 500 <= response.status < 600:
                    raise aiohttp.ClientError(f"Server error: {response.status}")
        except aiohttp.ClientError as e:
            print(f"Attempt failed: {e}")
            if attempt == retries - 1:
                return None

async def send(url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100):
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return [response for response in responses if response]

async def main() -> None:
    url = 'https://httpbin.org/get'
    successful = await send(url)
    print(successful)

if __name__ == "__main__":
    asyncio.run(main())
