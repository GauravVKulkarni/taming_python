# simulates bulk api calls immediately halted after one api call takes longer than expected

import asyncio
import random

async def fake_call(i):
    print(f'started {i + 1}')
    await asyncio.sleep(random.randint(0,8))
    print(f'completed {i + 1}')

async def main():
    try:
        async with asyncio.timeout(4):
            async with asyncio.TaskGroup() as tg:
                for i in range(10):
                    tg.create_task(fake_call(i), name=f'task {i+1}')
    except asyncio.TimeoutError:
        print("Abort")

if __name__ == '__main__':
    asyncio.run(main())