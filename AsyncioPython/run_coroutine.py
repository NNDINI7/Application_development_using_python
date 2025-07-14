import asyncio
async def main():
    print("hello world....")
    asyncio.sleep(2)
    print("Goodbye !!")
   
# async def main():
#     print("Start of main coroutine")

print(type(main())) # coroutine object
# main() returns a coroutine object, which is then run by asyncio.run()

# run the main coroutine
asyncio.run(main())

# RuntimeWarning: coroutine 'sleep' was never awaited
