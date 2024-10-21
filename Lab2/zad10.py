import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.1758&longitude=19.5707&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    data = await fetch(url)
    temperatures = data["hourly"]["temperature_2m"]
    average_temp = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)

    text = (
        f"Srednia temperatura: {average_temp:}\n"
        f"Minimalna temperatura: {min_temp:}\n"
        f"Maksymalna temperatura: {max_temp:}\n"
    )

    with open("file.txt", 'w') as f:
        f.write(text)

if __name__ == "__main__":
    asyncio.run(main())

