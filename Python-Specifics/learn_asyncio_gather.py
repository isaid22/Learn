import asyncio

async def worker(id):
    await asyncio.sleep(1)
    return f"Worker {id} done"

async def main():
    # Use gather instead of TaskGroup for Python < 3.11
    results = await asyncio.gather(worker(1), worker(2))
    print(results)

if __name__ == "__main__":
    asyncio.run(main())