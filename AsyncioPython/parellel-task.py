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
    coroutine1 = asyncio.create_task(fetch_data(3,1))
    coroutine2 = asyncio.create_task(fetch_data(5,2))
    coroutine3 = asyncio.create_task(fetch_data(3,3))
    print("Coroutine created, now running...")
    # run the coroutine and wait for its completion
    result1 = await coroutine1
    print("Coroutine completed with result:", result1)
    result2 = await coroutine2
    print("Coroutine completed with result:", result2)
    result3 = await coroutine3
    print("Coroutine completed with result:", result3)


# run the main coroutine
asyncio.run(main())
