import asyncio

async def say_after(delay, what):
    """An asynchronous coroutine that waits then prints a message."""
    await asyncio.sleep(delay) # Yields control to the event loop
    print(what)

async def main():
    print(f"Started at ...")
    
    # Schedule two tasks concurrently
    task1 = asyncio.create_task(say_after(2, 'hello'))
    task2 = asyncio.create_task(say_after(1, 'world'))
    
    # Wait for both tasks to complete
    await task1
    await task2
    
    print(f"Finished at ...")

if __name__ == "__main__":
    import time
    start_time = time.perf_counter()
    asyncio.run(main()) # Starts the event loop
    end_time = time.perf_counter()
    print(f"Total time elapsed: {end_time - start_time:.2f} seconds")
