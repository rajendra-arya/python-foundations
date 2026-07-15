from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total+=i
    print("Done✅")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"Time Taken : {time.time() - start:.2f} seconds")

# Output
# Crunching some numbers...
# Crunching some numbers...
# Done✅
# Done✅
# Time Taken : 1.95 seconds

# it performed better than from threads(2.60 seconds)