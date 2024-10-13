import asyncio


async def main() -> None:
    i = 1
    while i < 6:
        print(i)
        await asyncio.sleep(1)
        i +=1


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())