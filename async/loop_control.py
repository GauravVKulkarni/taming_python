import asyncio

async def fun():
    print("Started running async function.")
    await asyncio.sleep(2)
    print("Finished async function.")

async def not_fun():
    task = asyncio.create_task(fun())
    await task

if __name__ == "__main__":

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    
    # loop.run_until_complete(task)
    # loop.run_until_complete(fun())
    loop.run_until_complete(not_fun())
    loop.close()