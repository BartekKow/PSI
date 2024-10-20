import aiohttp
import asyncio


async def fetch_weather(latitude: float, longitude: float) -> dict:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    cities = {
        "Porlamar": (10.95, -63.86),
        "Moroni": (-11.70, 43.24),
        "Helsinki": (60.17, 24.94)
    }
    results = await asyncio.gather(*(fetch_weather(*coords) for coords in cities.values()))
    weather_data = {city: result["current_weather"]["temperature"] for city, result in zip(cities.keys(), results) if
                    "current_weather" in result}
    print(weather_data)


if __name__ == "__main__":
    asyncio.run(main())