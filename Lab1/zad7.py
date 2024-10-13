import asyncio

async def main() -> None:
    await asyncio.gather(
        przepis("salatka"),
        przepis("tosty"),
        przepis("zupa")
    )

async def krojenie(nazwa) -> None:
    print(f"{nazwa}: krojenie rozpoczęte")
    await asyncio.sleep(2)
    print(f"{nazwa}: krojenie zakończone")

async def gotowanie(nazwa) -> None:
    print(f"{nazwa}: gotowanie rozpoczęte")
    await asyncio.sleep(5)
    print(f"{nazwa}: gotwanie zakończone")

async def smazenie(nazwa) -> None:
    print(f"{nazwa}: smażenie rozpoczęte")
    await asyncio.sleep(3)
    print(f"{nazwa}: smażenie zakończone")

async def przepis(potrawa) -> None:

    if potrawa == "salatka":
        await krojenie(potrawa)

    elif potrawa == "tosty":
        await smazenie(potrawa)

    elif potrawa == "zupa":
        await krojenie(potrawa)
        await gotowanie(potrawa)

    print(f"{potrawa}: potrawa gotowa")

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())