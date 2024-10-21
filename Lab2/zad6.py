import aiohttp
import asyncio


async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


def filter_forecast(forecast: dict, mask: dict) -> bool:
    current = forecast.get('current', {})
    for key, condition in mask.items():
        variable = current.get(key)
        if variable is None:
            return False

        operator, number = condition[0], float(condition[1:])
        if (operator == "<" and variable >= number) or (operator == ">" and variable <= number):
            return False
    return True


async def main() -> None:
    url1 = "https://api.open-meteo.com/v1/forecast?latitude=10.57&longitude=-63.50&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url2 = "https://api.open-meteo.com/v1/forecast?latitude=-11.42&longitude=43.15&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    url3 = "https://api.open-meteo.com/v1/forecast?latitude=60.10&longitude=24.56&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    weather = await asyncio.gather(fetch(url1), fetch(url2), fetch(url3))

    mask = {
        "wind_speed_10m": "<20",
        "temperature_2m": ">26"
    }

    cities = {
        "Porlamar": weather[0],
        "Moroni": weather[1],
        "Helsinki": weather[2],
    }

    filtered_forecast = {
        city: forecast["current"]
        for city, forecast in cities.items()
        if filter_forecast(forecast, mask)
    }
    print(filtered_forecast)

if __name__ == "__main__":
    asyncio.run(main())



