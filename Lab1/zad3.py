import asyncio


async def main() -> None:
    await asyncio.sleep(3)
    print("Hello")

async def main2() -> None:
    await asyncio.sleep(2)
    print("World")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
        runner.run(main2())