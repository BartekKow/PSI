import aiohttp
import asyncio

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

def average(weather: dict) -> float:
    total_temp = 0
    for i in range(24, 48):
        total_temp += weather["hourly"]["temperature_2m"][i]
    return total_temp/24

async def main() -> None:
    #Berlin
    url1 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.405&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    #Londyn
    url2 = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    #Madryt
    url3 = "https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    weather = await asyncio.gather(fetch(url1), fetch(url2), fetch(url3))

    dictionary = {}
    for i in range(len(weather)):
        dictionary[average(weather[i])] = {str(weather[i]["current"])}
    sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
    print(dictionary)

if __name__ == "__main__":
    asyncio.run(main())


