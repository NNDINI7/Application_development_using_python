import asyncio


# A shared resource
shared_resource = 0


# An asynchronous lock
lock = asyncio.Lock()


async def modify_shared_resource(id):
    global shared_resource
    async with lock:
        print("#"*40)
        print(f"{id}:Resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(2)  # Simulate a long-running task / IO operation
        print(f"{id}:Resource after modification: {shared_resource}")


async def main():
    await asyncio.gather(*(modify_shared_resource(i+1) for i in range(5)))


asyncio.run(main())

