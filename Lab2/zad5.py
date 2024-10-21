import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url1 = "https://api.open-meteo.com/v1/forecast?latitude=10.57&longitude=-63.50&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url2 = "https://api.open-meteo.com/v1/forecast?latitude=-11.42&longitude=43.15&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url3 = "https://api.open-meteo.com/v1/forecast?latitude=60.10&longitude=24.56&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    weather = await asyncio.gather(fetch(url1),fetch(url2),fetch(url3))

    weather_dict = {
        "Porlamar": weather[0]["current"],
        "Moroni": weather[1]["current"],
        "Helsinki": weather[2]["current"],
    }
    print(weather_dict)

if __name__ == "__main__":
    asyncio.run(main())