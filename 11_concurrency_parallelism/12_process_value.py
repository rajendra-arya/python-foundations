from multiprocessing import Process, Value

def increment(counter):
    for _ in range(1000):
        with counter.get_lock(): # automatically gets lock and wait for completion then locks next process 
            counter.value+=1 #this shared data will be used by all process

# Create shared state
if __name__ == "__main__":
    counter = Value("i",0) #creates shared memory in key value pair

    #create 4 processes
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)] 
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f"Final Counter value: {counter.value}") #value jst gives the value of counter obj

# output
# Final Counter value: 4000