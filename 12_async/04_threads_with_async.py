import time
import asyncio
from concurrent.futures import ThreadPoolExecutor #execute all threads in the pool, almost similar to asyncio.gather but for threads

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation # freeze specific thread for 3 sec
    return f"{item} stock : 33" #returns and goes back to idle pool

async def main():
    loop = asyncio.get_running_loop() # grabs the ref of event loop
    with ThreadPoolExecutor() as pool: # alot a pool of threads waiting for work
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai") #hands func with arg to idle thread in the pool
        result2 = await loop.run_in_executor(pool, check_stock, "Masala Chai") #hands func with arg to idle thread in the pool
        print(result) #main event loop prints it after catching and assigning
        print(result2)
asyncio.run(main())

# output (u won't see much difference in the output)
# Checking Masala Chai in store...
# Masala Chai stock : 33

