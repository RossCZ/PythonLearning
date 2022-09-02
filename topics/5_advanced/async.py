import asyncio
import time


async def lag_print(delay, what):
    await asyncio.sleep(delay)
    print(f"printing: {what}")
    return f"Result of {what, delay}"


async def async_example():
    print(f"start time: {time.strftime('%X')}")

    slow_task = asyncio.create_task(lag_print(3, "hello"))
    fast_task = asyncio.create_task(lag_print(1, "world"))

    # run tasks individually
    await slow_task
    print(f"time: {time.strftime('%X')}")  # wont be executed "in between" as we are still waiting for the slow task
    res = await fast_task  # save result to a variable
    print(res)

    # use gather function
    # results = await asyncio.gather(slow_task, fast_task)
    # print(results)

    # or create and run tasks directly
    # await asyncio.gather(lag_print(2, "hello"), lag_print(1, "world"))

    print(f"end time: {time.strftime('%X')}")


asyncio.run(async_example())  # .py file
# await async_example()  # Jupyter
