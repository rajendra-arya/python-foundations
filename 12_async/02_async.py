import asyncio
import time

async def brew(name):
    start = time.time()
    print(f"Brewing {name}...")
    await asyncio.sleep(3)
    # time.sleep(3)
    end = time.time()
    print(f"\t{name} is ready in {end-start:.2f}.")

async def main(): #it can also be a coroutine
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Lemon Chai")
    )


start = time.time()
asyncio.run(main())
end = time.time()
print(f"Total Time taken: {end-start:.2f}")


# with await asyncio.sleep()
# Brewing Masala Chai...
# Brewing Lemon Chai...
#         Masala Chai is ready in 3.01.
#         Lemon Chai is ready in 3.01.
# Total Time taken: 3.01


# with threading
# Brewing Masala...
# Brewing Lemon...
#         Masala is ready in 3.00.
#         Lemon is ready in 3.00.
# Total Time taken: 3.00



# with time.sleep(3)
# Brewing Masala Chai...
#         Masala Chai is ready in 3.00.
# Brewing Lemon Chai...
#         Lemon Chai is ready in 3.00.
# Total Time taken: 6.01



### threading example
# import threading

# def brew(name):
#     start = time.time()
#     print(f"Brewing {name}...")
#     time.sleep(3)
#     end = time.time()
#     print(f"\t{name} is ready in {end-start:.2f}.")

# start = time.time()
# threads = [threading.Thread(target=brew, args=(tea, )) for tea in ["Masala", "Lemon"]]
# [t.start() for t in threads]
# [t.join() for t in threads]

# # asyncio.run(main())
# end = time.time()
# print(f"Total Time taken: {end-start:.2f}")