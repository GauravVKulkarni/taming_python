import asyncio
import time

async def sleeper(n,t):
    print(f"{n} has slept for {t} seconds.")
    await asyncio.sleep(t)
    print(f"{n} just woke up after {t} seconds of sleep.")

async def sleep_manager():
    await asyncio.gather(
        sleeper(1, 5),
        sleeper(2, 3),
        sleeper(3, 7)
    )

if __name__ == '__main__':
    t = time.time()

    asyncio.run(sleep_manager())

    print(f"Took {(time.time() - t):.2f} seconds")