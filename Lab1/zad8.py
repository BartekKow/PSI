import asyncio

async def main() -> None:
    await asyncio.gather(
        przetwarzanie(1),
        przetwarzanie(2),
        przetwarzanie(3),
        przetwarzanie(4),
        przetwarzanie(5)
    )

async def wczytywanie(plik) -> None:
    await asyncio.sleep(2)
    print(f"{plik}: wczytywanie zakończone")

async def analiza(plik) -> None:
    await asyncio.sleep(4)
    print(f"{plik}: analizowanie zakończone")

async def zapis(plik) -> None:
    await asyncio.sleep(1)
    print(f"{plik}: zapisywanie zakończone")

async def przetwarzanie(plik) -> None:
    await wczytywanie(plik)
    await analiza(plik)
    await zapis(plik)

if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())