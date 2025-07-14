
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
    # create a coroutine object for fetch_data with a delay of 2 seconds
    result = await asyncio.gather(
        fetch_data(3, 1),
        fetch_data(5, 2),
        fetch_data(3, 3)
    )

    for i, res in enumerate(result):
        print(f"Coroutine {i+1} completed with result:", res)


# run the main coroutine
asyncio.run(main())
