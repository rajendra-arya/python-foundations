import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0 #same memory location so gil(mutex) comes in actions
    for _ in range(10_00_00_000):
        count+=1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 = threading.Thread(target=brew_chai, name="Barista-1")

thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()

print("Total time taken: {:.2f} seconds.".format(end - start))


# Ouput(threading)
# Barista-1 started brewing...
# Barista-2 started brewing...
# Barista-2 finished brewing...
# Barista-1 finished brewing...
# Total time taken: 20.18 seconds.