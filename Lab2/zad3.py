from typing import Tuple

import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main() -> None:
    users = await foo()
    print(users)

async def foo() -> tuple[dict, dict, dict, dict, dict]:
    return await asyncio.gather(
        fetch("https://api.spacexdata.com/v4/launches/latest"),
        fetch("https://official-joke-api.appspot.com/random_joke"),
        fetch("https://dog.ceo/api/breeds/image/random"),
        fetch("https://api.coindesk.com/v1/bpi/currentprice/BTC.json"),
        fetch("https://catfact.ninja/fact")
    )

if __name__ == "__main__":
    asyncio.run(main())
