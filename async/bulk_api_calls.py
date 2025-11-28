# Note - Don't abuse and overload free, public APIs

# calling an api multiple times concurrently

import asyncio
import aiohttp

url = "https://api.toys/api/coin_flip"

async def call(session, i):
    async with session.get(url) as res:
        data = await res.json()
        print(f"[{i + 1}] : {data['result']}")


async def main():
    async with aiohttp.ClientSession() as session:
        try:
            async with asyncio.TaskGroup() as tg:
                for i in range(5):
                    tg.create_task(call(session, i))
        except* Exception:
            print("Abort. a call failed.")


if __name__ == '__main__':
    asyncio.run(main())