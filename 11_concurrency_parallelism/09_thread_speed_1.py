import threading
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total+=i
    print("Done✅")

threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

start = time.time()
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time Taken : {time.time() - start:.2f} seconds")

# Output
# Crunching some numbers...
# Crunching some numbers...
# Done✅
# Done✅
# Time Taken : 2.50 seconds