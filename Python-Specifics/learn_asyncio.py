import asyncio

async def my_coroutine(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} finished")

async def main():
    # Schedule both tasks immediately
    task1 = asyncio.create_task(my_coroutine("A", 1))
    task2 = asyncio.create_task(my_coroutine("B", 1))

    # They run concurrently while we wait
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())