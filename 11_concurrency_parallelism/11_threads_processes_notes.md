# Concurrency
- doing multi tasking by switching task one at a time
- switching task
- limited cores(cpu)(eg.1 core multiple task)
- eg. 1 chef cooking 2 different meal
- graph of mutli tasking(P1,P2,P3)  with execution time:
    ```raw
    |    _
    |  _  _
    | _     _
    |__________
    execution time
    ```
- builtin modules to perform concurrency in python
    1. threading.Thread (builtin)
    2. asyncio


## multi threading
- 2 threads - simple words segregating tasks to 2 diferent people
- technically 1 core is engaged and multiple threads which are switched frequently and performing the task
- threads  - it should also have a target
- join() - wait all threads together and show results when everything is done

- ```py
    # 2 threads - segerating  task to 2 difrent people

    #create threads  - it should have a target
    order_thread = threading.Thread(target=take_orders)
    brew_thread = threading.Thread(target=brew_chai)

    #invoke them or start thread
    order_thread.start()
    brew_thread.start()

    # multi threading - have to wait for all perform to complete and the move next
    order_thread.join()
    brew_thread.join()

    print('All orders takend and chai is brewed')


    # Taking order for #1
    #          Brewing chai for #1 -wait for 3s
    # Taking order for #2
    # Taking order for #3
    #          Brewing chai for #2 - after 3s
    #          Brewing chai for #3  - after 6s
    # All orders taken and chai is brewed
    ```




# Parallelism
- doing work in parallel i.e doing multiple tasks together at the same time.
- multiple cores(eg. each core 1 task)
- eg. 2 chef cooking 2 different meal
    - when processing a long vdo , divide in chunk and assign it to muliple cores and then combine the results and process it for returning the result
    - issue: if one core get bsy(because of some reason,like os bg task) so it can delay the whole final output.
- graph of mutli tasking(P1,P2,P3) with execution time:
    ```raw
    |________P1
    |________P2
    |________P3
    |__________
    execution time
    ```
- builtin modules to perform concurrency in python
    1. multiprocessing.Process
    2. concurrent.futures.ProcessPoolExcecutor

-  Create the process instance :
    `multiprocessing.Process(target=function, args=(arguments)")` 
process_variable = multiprocessing.Process(
        target=function_name, 
        args=("value1", "value2")
    )

- ```py

    from multiprocessing import Process
    import time

    def brew_chai(name):
        print(f"Start of {name} chai brewing")
        time.sleep(3)
        print(f"\tEnds of {name} chai brewing")

    if __name__ == "__main__":
        #Create the process instance
        chai_makers = [
            Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
            for i in range(3)
            ]
        
        # Start all Process
        for p in chai_makers: #chaimakers -> [1brew chai, 2brew chai , 3 brewchai] 
            p.start()

        # wait for all to complete
        for p in chai_makers:
            p.join()
        
        print("All Chai Served. Thank You!")

    # Start of Chai Maker #1 chai brewing
    # Start of Chai Maker #2 chai brewing
    # Start of Chai Maker #3 chai brewing
    #         Ends of Chai Maker #1 chai brewing
    #         Ends of Chai Maker #2 chai brewing
    #         Ends of Chai Maker #3 chai brewing
    # All Chai Served. Thank You!

    # you have 3 waiters in the restaruant now, all take order , wait for order to finish, and pick and serve the order to the customer.
    # so everyone doing work at the same time.

    ```

# GIL - Global Interpreter Lock
- The GIL is a default mutual exclusion lock operating behind the scenes. 
- reserve the memmory for a thread until its job is done.
- locks the memmory so no other thread can access it
- mutex (mutual exclusion) : its pythons mutually exclusive locking system
    - once a thread reaches a memmory location it gets this mutex lock so no other thread can access the memmory.
    - once its job is done , it release the mutex lock so next thread can accuire and it and proceed.
    - **_A mutex (mutual exclusion) is a synchronization primitive used in Python's threading module to grant exactly one thread access to a shared resource at a time, preventing race conditions and data corruption._**
    - The Real-World Analogy :Think of a single-occupancy public restroom with a key at the service counter:The key is mutual because every customer uses the exact same key.The key provides exclusion because holding it guarantees you are the only person inside.
    - mutual - same memmory , exclusive - when using its exlcusive

- *Race Condition : 
    - where 2 threads wants to access same memmory location and want to modify it at the same time. 
    - almost all db have the race conditions and there are mechanism to avoid them.
- real life example :  1 order can be placed at a time in a counter irrsepctive of no. of baristas.
- when to use gil(using threading) and when to bypass(using multiprocessing) it is the decision u should know.
- sytnax
    ```py
    #gil threading
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
    
    ```
- syntax bypassing gil:
    ```py
    from multiprocessing import Process
    import time

    def crunch_number():
        print(f"Started the count process...")
        count = 0
        for _ in range(10_00_00_000):
            count+=1
        print(f"Ended the count process...")


    if __name__ == "__main__":
        start = time.time()
        p1 = Process(target=crunch_number) #overiding the mutex
        p2 = Process(target=crunch_number)

        p1.start()
        p2.start()
        p1.join()
        p2.join()

        end = time.time()

        print(f"Total time with multi-processing is {end-start:.2f} seconds.")



    # output(without gil)
    # Started the count process...
    # Started the count process...
    # Ended the count process...
    # Ended the count process...
    # Total time with multi-processing is 14.39 seconds.


    # main method 
    # - its fine for thread
    # - they know there entry point

    # RuntimeError if u dont use main in the multiprocessing: 
    # An attempt has been made to start a new process before the
    # current process has finished its bootstrapping phase.
    # This probably means that you are not using fork to start your
    # child processes and you have forgotten to use the proper idiom
    # in the main module:
    # - it means u dont have main,which is a freeze support
    ```
- `main` method Runtime Error:
    - thread doesnt need main :
        - Entry point: Not required. 
        - in concurrency its automatically know the entry point, so it works without explicitly writing it.
    - mulitprocessng need main :
        - Entry point: required. 
        - for parallelism you need to explicitly write main to avoid error. 
    - error:
        ```py
        # RuntimeError if u dont use main in the multiprocessing: 
        # An attempt has been made to start a new process before the
        # current process has finished its bootstrapping phase.
        # This probably means that you are not using fork to start your
        # child processes and you have forgotten to use the proper idiom
        # in the main module:
        # - it means u dont have main,which is a freeze support
        ```
- Quick Summary
    - When it is good: For I/O-bound tasks (web scraping, file downloads, API calls) and single-threaded apps. It keeps code fast, simple, and safe.
    - When to bypass: For CPU-bound tasks (data crunching, video processing, heavy math) where you need to use multiple CPU cores simultaneously.
    - How to bypass: Use the multiprocessing module, leverage optimized libraries like NumPy, or use Python 3.13+'s new experimental free-threaded mode.
        - The experimental free-threaded mode (introduced via PEP 703) is an alternative version of Python that completely removes the Global Interpreter Lock (GIL). need to learn more about.


# Thread
- Proccess vs Threads
    - OS basics :
        - > [Program(with lots of instructions) in Disk]  
            - > [(prg can work with multiple process) in RAM]
                - > [(each process can be divided into multiple threads)in Process]
        - process 
            - **Process consists of multiple Threads**
            - each process gets its code, registers, slack, counter, data is shared
            - research more
            - single threaded process
            - multi threaded process

- there is one process(main) having multiple threads, remember its a 1 core(CPU) only
- thread can share memory because they are all in one process itself.
- when threading is not affective?
    - when computation is beng done
- io opertation
    - i/o bound task  : disk read adn write
    - web request - no memmory sharng


## threading for io bound (like downloading)
    - disk read/write
    - web request (each thread will request serve idivdually)
        - thread request server and wait for response
        - during this time another thread makes request
        - since all of them will be writing the response in different memory location
        - so each thread writes on different memory
        - therefore it speed up the process of i/o bound operation(eg. downloading).


## thread lock
- threading.Lock() - ensures only one thread can modify the shared data at a time.
- without lock u may get incorrect results due to the race conditions.
-`with` -  safe the memory from other threads
- makes the program thread safe.
- its better to use lock, when u know threads might can manipulate the data(var).
- good practice: use `lock` to change desired variable so we wont encounter race condition.
- ```py
    counter +=1 #without lock
    # higly recommended
    with lock: #locks current mem loc for us 
            counter +=1
    ```
- ```py

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

    # need to ponder.. :  research
    #   stmt: if u remove the with lock here, u wont see much difference in the output because python improves it in bts.  
    ```



# Multi Processing using thread and Process speed analysis
- ```py
    # file: \09_thread_speed_1.py  
    #with Threads
    Crunching some numbers...
    Crunching some numbers...
    Done✅
    Done✅
    Time Taken : 2.60 seconds

    # file: \10_process_speed_2.py  
    # with Process        
    Crunching some numbers...
    Crunching some numbers...
    Done✅
    Done✅
    Time Taken : 1.95 seconds
    ```

# Process
- In multi processing Each process gets its own memory
- in multiprocess there is no sharing of the memory.(threads can share memory)
- to fix this the communication problem in processes 
    - we use `queues`, `values`, pipes etc which can be responsible for sharing the memory.

## Queue - shared state
- it solves communication problem in process by sharing memory
- same like data structure in queue , array on steroid
- multiprocessing provides queue themselves
- how it works?
    - it will put the data in a new data structure which is queue
    - it will be passed as an argument in Process, which can be single or muliple methods/process
- ```py

    from multiprocessing import Process, Queue

    def prepare_chai(queue):
        #add data in queue
        queue.put("Masala Chai is ready.")
        queue.put("Masala Chai is not ready.")
        

    if __name__ == "__main__":
        # generate the queue, it will be passed
        queue = Queue()
        # pass queue obj as argument for storing data
        p = Process(target=prepare_chai, args=(queue,))
        p.start()
        p.join()
        while not queue.empty():
            print(queue.get())


    ```


## Value - shared state
- it solves communication problem in process by sharing memory in multi processes
- its a key value pair
- it automatically gets the lock using `get_lock()`
    - which locks one process till completion and move to next and repeat

```py
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
```

- The processing used in lot of places in image processing, ai training scripts etc
- people do multiprocessing along with threading as well.


## Python Concurrency Cheat Sheet
## 🧵 Multithreading (I/O-Bound)
- Core Concept: Shares memory space, handles idle waiting time.
- Limitation: Blocked by Python's GIL (cannot run true parallel CPU math).
- Key Applications:
- Web Scraping / Downloading: Fetching thousands of images or text datasets from the cloud simultaneously.
   - Live Video Streaming: Grabbing raw video packets from an IP camera stream without dropping frames.
   - API Requests: Sending parallel requests to external AI model endpoints (e.g., OpenAI, Hugging Face). [7, 8] 

## ⚙️ Multiprocessing (CPU-Bound)

- Core Concept: Spawns separate memory spaces, runs true parallel math across multiple CPU cores. [9, 10, 11] 
- Limitation: High RAM usage; data must be "pickled" (serialized) to pass between processes. [12, 13] 
- Key Applications:
- Batch Image Augmentation: Rotating, cropping, and flipping millions of training photos simultaneously.
   - Video Decoding: Extracting and parsing heavy H.264 video frames into raw NumPy arrays.
   - Feature Extraction: Computing pixel histograms or tokenizing massive text datasets before AI training.

## 🔀 Hybrid Pipelines (Combined Workloads)

- Core Concept: Threads handle data ingestion (input) while Processes handle data transformation (math). [14, 15] 
- How They Work Together: Threads pull data from the network/disk into memory, then immediately hand it off to Processes to crunch the data without blocking the input stream. [16] 
- Key Applications:
    -  Self-Driving Car Vision: One thread continuously captures raw camera feeds while multiple background processes execute object detection models.
   - ETL(extract transform and load) Data Pipelines: Threads stream raw data archives from the web while separate processes instantly unzip, clean, and format them.
   - Real-time AI Audio: A lightweight thread listens to a live microphone buffer while an isolated process runs the heavy voice-to-text model.

    

# The Core Difference
```
                                [ Concurrency ]
                                        │
                    ┌───────────────────┴───────────────────┐
                    ▼                                       ▼
        [ Multithreading / Async ]                 [Multiprocessing ]
        (Dealing with lots of tasks)               (Doing lots of tasks)
        (Interleaved on 1 core)                    (Parallel on multiple cores)
```


||Multithreading |Multiprocessing|
|-|-|-|
|Concurrency | by Interval (Interleaved)| Without Intervals (Parallel)|
|How it works: |A single CPU core switches back and forth between tasks at rapid intervals (context switching). | Multiple CPU cores run completely separate tasks at the exact same physical millisecond. |
||It looks simultaneous to humans, but it is actually just high-speed multitasking on a timeline.| There are no intervals or pauses to share a processor because every task has its own dedicated hardware core.|
| The Visual:| Task 1 -> Pause -> Task 2 -> Pause -> Task 1| Core 1: Task 1(Continuous), Core 2: Task 2(Continuous)|
|
