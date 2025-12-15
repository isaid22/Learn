### Requires Python 3.11+
import asyncio

async def worker(id):
    await asyncio.sleep(1)
    return f"Worker {id} done"

async def main():
    # Recommended approach: TaskGroup (Python 3.11+)
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(worker(1))
        t2 = tg.create_task(worker(2))
    
    # Results are available after the TaskGroup block
    print(t1.result(), t2.result())

if __name__ == "__main__":
    asyncio.run(main())