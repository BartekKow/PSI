import asyncio
import math


async def main() -> None:
    await asyncio.gather(
        praca(1),
        praca(2),
        praca(3)
    )

async def maszyna(numerMaszyny) -> None:
    print(f"Maszyna {numerMaszyny}: start cyklu")
    if numerMaszyny == 1:
        await asyncio.sleep(2)
    elif numerMaszyny == 2:
        await asyncio.sleep(3)
    elif numerMaszyny == 3:
        await asyncio.sleep(5)
    print(f"Maszyna {numerMaszyny}: koniec cyklu")

async def praca(numerMaszyny):
    i = 0
    if numerMaszyny == 1:
        while i < math.floor(15/2):
            await maszyna(numerMaszyny)
            i = i+1

    elif numerMaszyny == 2:
        while i < math.floor(15/3):
            await maszyna(numerMaszyny)
            i = i+1

    elif numerMaszyny == 3:
        while i < math.floor(15/5):
            await maszyna(numerMaszyny)
            i = i+1

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
