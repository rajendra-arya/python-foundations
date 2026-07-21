# Simple application of threading and async working together

import asyncio
import threading
import time

# Background thread worker
def background_worker():
    while True:  #will run forever
        time.sleep(1) # Block the background thread for 1 second
        print("Logging the system health 🕟")

# Main thread async worker
async def fetch_order():
    await asyncio.sleep(3) #   # Non-blocking pause for 3 seconds within the event loop
    print("Order is fetched.🚚")

threading.Thread(target=background_worker, daemon=True).start()
asyncio.run(fetch_order())
# Logging the system health 🕟
# Logging the system health 🕟
# Order is fetched.🚚

asyncio.run(fetch_order())
threading.Thread(target=background_worker).start()
# output
# Order is fetched.🚚