import asyncio

n = int(input("Podaj liczbe N: "))
async def main() -> None:
    i = 0
    x = 0
    y = 1
    z = 0

    while i < n:
        print(z)
        await asyncio.sleep(1)
        z = x + y
        y = x
        x = z
        i += 1




if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())