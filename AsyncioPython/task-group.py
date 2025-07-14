import asyncio

# define a couroutine that simulates a long-running task
async def fetch_data(delay, id):
    print(f"Fetching data with a delay of {delay} seconds for ID: {id}...")
    await asyncio.sleep(delay)  # simulate an I/O-bound operation
    print(f"Data fetched after {delay} seconds for Id: {id}!")
    return f"Data from {delay} seconds delay for ID: {id}"

# Define the main coroutine that runs coroutine
async def main():
    print("Start of main coroutine")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([3, 5, 3], start=1):
            task = tg.create_task(fetch_data(sleep_time, i))
            tasks.append(task)

    # After the TaskGroup completes, we can gather results
    result = [task.result() for task in tasks]
    # result = [task.result() for task in tasks if not task.cancelled() and not task.exception()]

    for i, res in enumerate(result):
        print(f"Coroutine {i+1} completed with result:", res)


# run the main coroutine
asyncio.run(main())
