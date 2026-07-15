# using lock to handle shared state
import threading

counter = 0

lock = threading.Lock()

def increment(): #create a thread safe method
    global counter
    for _ in range(100000):
        with lock: #locks current mem loc for us (Recommended)
            counter +=1

threads = [threading.Thread(target=increment) for _ in range(10)]

#create comprehension for start and join of thread 
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final Counter: {counter}")



# output:
# Final Counter: 1000000


# # using lock
#     - only one thread modifes the share data at a time
#     - without the lock u may get incorrect result due to the race condition