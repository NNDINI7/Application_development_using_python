import asyncio

# define a couroutine that simulates a long-running task
async def fetch_data(delay):
    print(f"Fetching data with a delay of {delay} seconds...")
    await asyncio.sleep(delay)  # simulate an I/O-bound operation
    print(f"Data fetched after {delay} seconds!")
    return f"Data from {delay} seconds delay"

# Define the main coroutine that runs coroutine
async def main():
    print("Start of main coroutine")
    # create a coroutine object for fetch_data with a delay of 2 seconds
    coroutine = fetch_data(5)
    print("Coroutine created, now running...")
    # run the coroutine and wait for its completion
    result = await coroutine
    print("Coroutine completed with result:", result)


# define the main coroutine that runs multiple fetch_data coroutines concurrently
# async def main():
#     delays = [1, 2, 3]  # list of delays for each fetch_data call
#     tasks = [fetch_data(delay) for delay in delays]  # create a list of coroutine tasks
#     results = await asyncio.gather(*tasks)  # run all tasks concurrently and wait for their completion
#     print("All data fetched:", results)


# run the main coroutine
asyncio.run(main())
