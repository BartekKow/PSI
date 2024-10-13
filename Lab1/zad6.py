import asyncio
import random

async def fetch(delay: int) -> None:
    await asyncio.sleep(delay)
    print(random.randint(0,100))


async def foo() -> None:
    await asyncio.gather(
        fetch(0),
        fetch(1),
        fetch(2),
        fetch(3),
        )

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(foo())