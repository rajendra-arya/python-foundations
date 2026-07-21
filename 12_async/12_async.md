# Async Python
- it's also do multiprocessing like multithreading or multiprocessing
- it declares a coroutine function.

    -   || Regular Functions (Hierarchy) | Coroutines (No Hierarchy) |
        |---|---|---|
        | Naming Reason | Sub-routine: Subordinate task controlled by a caller. | Co-routine: Co (Cooperative - sharing control) + Routine (Function). |
        | Execution Flow | Single Entry & Exit: Starts at line one, exits at return. | Multiple Pause Points: Stops at any `await` or `yield` and resumes later. |
        | Memory Behavior | Stack Memory Control: Automatically erases all data when finished. | Persistent State: Keeps its data alive in memory while paused. |
        | Code Example | `def greet(): return "Hello"` | `async def greet(): await asyncio.sleep(1)` |

- example:  fetch 10 web pg
- python handles lot of things in the background by itself
- syntax :
    - `async def funcname`: it declares a **coroutine**(special function that can be paused)
        -  ability to cooperatively work with other routines (functions).
    - `await`: pauses execution until the result is ready.
        - it's a **non blocking operation**
        - await means u will wait but in non blocking fashion.
    - `asyncio`: builtin python library
    -  **Event Loop**: The engine that runs and schedule co-routine.
        - when function is ready for execution it informs the event loop for execution
        - Event loopchecks constantly is there someone which need to execute(if job done, infrom me i will execute you).
        - event loop -> await -> time.sleep(7) 
            - event loop will keep a check on it and when it finished it will execute.


### `time.sleep(3) vs aysnc.sleep(3)`
- difference is in the foundation , how the code runs bts
- `time.sleep(3):` 
    - Blocks the entire thread. 
    - The CPU halts everything, freezes the whole program, and waits idly for 3 seconds.
    - it Communicates with the Operating System to freeze the thread.
    - The entire application becomes unresponsive during the wait.
    
    - Analogy: Staring at the oven waiting for bread to bake.
    
- `asyncio.sleep(3):` 
    -Yields control(temporarily gives up control). 
    - The function pauses, but the event loop immediately switches to run other ready tasks during those 3 seconds
    - it Communicates with the Python Event Loop to switch tasks.
    - The application remains highly responsive and processes other data.
    - Setting a timer and chopping vegetables while the bread bakes.


## how async and threading is different?
- Both looks similar
- ```py 
    #file : 02_async.py

    ## with async and await asyncio.sleep(3)
    # Brewing Masala Chai...
    # Brewing Lemon Chai...
    #         Masala Chai is ready in 3.01.
    #         Lemon Chai is ready in 3.01.
    # Total Time taken: 3.01


    ## with threading and time.sleep(3)
    # Brewing Masala...
    # Brewing Lemon...
    #         Masala is ready in 3.00.
    #         Lemon is ready in 3.00.
    # Total Time taken: 3.00
    ```
<!-- do research --> 20"

- The Core Difference
    - asyncio (Asynchronous):
        - Runs on a single thread using an event loop. 
        - It cooperatively switches tasks when one task is waiting (like during await asyncio.sleep()).
        - ```py 
            # Runs both tasks concurrently on a single event loop
                await asyncio.gather(
                brew_chai("Masala", 3),
                brew_chai("Lemon", 3)
                )
            ```
    - threading (Multi-threading): 
        - Runs on multiple threads managed by the operating system. 
        - The OS switches between threads automatically.
        - ```py 
            #Creating two separate OS-level threads
            t1 = threading.Thread(target=brew_chai, args=("Masala", 3))
            t2 = threading.Thread(target=brew_chai, args=("Lemon", 3))
        ```
- **When to Use Which?**
    While both took 3 seconds for this time-delay simulation, they serve different purposes in real-world Python applications:
    - Use `asyncio` : 
        - when you have thousands of web requests, database queries, or network I/O operations. 
        - It uses way less memory because it doesn't create heavy OS threads.
    - Use `threading`:
        - when you are dealing with file operations (I/O) 
        - or web scraping where third-party libraries do not support async/await syntax.
    - _(Note: Neither of these speeds up heavy math or CPU-bound tasks in Python due to the Global Interpreter Lock (GIL). For heavy calculations, you need multiprocessing.)_

## aiohttp Library (non - blocking)
- it's an asynchronous http client/server framework - [official doc](https://docs.aiohttp.org/) 
- built on top of Python's asyncio.
- helps: 
    - to build web servers 
    - fetch data from external APIs without blocking the program's execution
- Concurrent Execution : 
    - Fetches all URLs at the same time. 
    - It fires all requests simultaneously.
    - doesn't happen in **requests library** as its sequential and blocking.
- Yields Controls: While waiting for a website to respond, it passes CPU control back to the event loop.

- ```py
    import asyncio
    import aiohttp
    import time

    url = "https://httpbin.org/delay/2" #gives response after the delay

    async def fetch_url(session , url):
        async with session.get(url) as response:
            print(f"Fetch {url} with status {response.status} ")


    async def main():
        urls = [url]*3  # 3* 2 sec delay means 6 sec total delay
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            await asyncio.gather(*tasks) #* spread operator in python like ... for unpacking multiple req

    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Operation took {end-start:.2f} seconds")

    # Output
    # Fetch https://httpbin.org/delay/2 with status 200 
    # Fetch https://httpbin.org/delay/2 with status 200 
    # Fetch https://httpbin.org/delay/2 with status 200 
    # Operation took 3.39 seconds

    ```

## Blocking vs Non-Blocking (Continueeeeeeeeeee)

| Feature | Blocking | Non-Blocking |
|-|-|-|
| Main Behavior | Stops the code execution completely. | Does not stop the code execution. |
| Resource Usage | The thread waits and does nothing. | The thread works on other tasks. |
| Python Code Example | time.sleep(2) | await asyncio.sleep(2) |
| Best Used For | Simple scripts, linear file processing. | Web servers, APIs, real-time apps. |


# Mixing threads with asyncio

- ayncio allows us to run async func on another thread run_in_executor.
- ThreadPool Executeor / almost similar to asyncio.gather but for threads
- run_in_executor : run in executor lets asyncio run async func on another thread without touching main(current) thread

- `concurrent.futures`: This is a built-in Python module. 
    - The word concurrent means "doing multiple things at the same time." 
    - The word futures represents a promise that a result will be given back to you later.

    - `ThreadPoolExecutor`: This is a specific class inside concurrent.futures module. 
        - It acts as the Manager. 
        - Its entire job is to create, manage, and destroy a group (a "pool") of background threads.
        - Why do we import it?
            - Standard `asyncio` does not know how to create threads on its own. 
            - We import `ThreadPoolExecutor` to give `asyncio` access to a team of synchronous background workers.

- `loop = asyncio.get_running_loop()`
    - **The Event Loop**: 
        - asyncio works because of a hidden engine running in the background called the Event Loop.
        - This loop acts like a traffic controller, constantly spinning and deciding which async task to run next.
    - `asyncio.get_running_loop()`: 
        - This function tells Python: 
        - "Look at the active async program right now, find the active traffic controller engine, and give me a reference to it."
    - Why do we need it?
        - To use an executor, you must use the method `loop.run_in_executor()`. 
        - Since that method belongs directly to the event loop object, you must **fetch the active loop first before** you can tell it to **hand jobs off to your threads**.
        
- **Summary**:
    - `ThreadPoolExecutor`: The toolkit used to build a team of background threads.asyncio.
    - `get_running_loop()`: The command used to grab the steering wheel(refrence) of the current async engine.
    - The Connection: 
        1. You grab the engine (loop), 
        2. hand it the team of threads (pool), and 
        3. say: loop.run_in_executor(pool, ...) to run your slow code.


- Example 
    ```py
    import asyncio
    import time
    from concurrent.futures import ThreadPoolExecutor #execute all threads in the pool, almost similar to asyncio.gather but for threads

    def check_stock(item):
        print(f"Checking {item} in store...")
        time.sleep(3) # Blocking operation
        return f"{item} stock : 33"

    async def main():
        loop = asyncio.get_running_loop() #designed for threads
        with ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, check_stock, "Masala Chai") #executes the thread
            print(result)

    asyncio.run(main())

    # output.l;
    # Checking Masala Chai in store...
    # Masala Chai stock : 33

    ```


##  Step-by-Step Code Execution Flow of above example
 
1. `asyncio.run(main())` :  initializes the system
    - Python fires up the single-threaded Event Loop engine and tells it to start executing the main() coroutine.
2. The loop registers itself: grabs the ref of event loop
    - The line `loop = asyncio.get_running_loop()` grabs a reference to that active engine so the code can talk to it directly.
3. The Thread Pool is created: alot a grp of threads waiting to work
    - The `with ThreadPoolExecutor() as pool`: the code block creates a group of synchronous background operating system threads that sit waiting for work.
    - The with block manages the lifetime of the thread pool and the boundaries.(consider with as a automatic door closer)
    - while the ThreadPoolExecutor actually creates the background threads.
4. The task is delegated: 
    - `loop.run_in_executor(pool, check_stock, "Masala Chai")` packages the synchronous function and its argument,
    - then hands them off to an idle worker thread in the pool.
5. The background thread executes: 
    - The worker thread immediately triggers print(), 
    - then hits `time.sleep(3)`, **freezing only that specific background thread for 3 seconds**.
6. The **main loop pauses but stays responsive**: 
    - The `await` keyword pauses execution at that line, telling the main Event Loop: 
        - _"Do not freeze the whole system; go handle other tasks while you wait."_
7. The background thread finishes: 
    - Once the 3-second sleep timer expires, the background worker wakes up, 
    - returns the stock string, and **goes back into the idle pool**.
8. The Event Loop resumes and cleans up: 
    - The main Event Loop catches the returned string, 
    - assigns it to result, 
    - prints it to the screen, 
    - exits the indentation, prompting the with statement to shut down the thread pool, and
    - safely closes the program.


# Asyncio and MultiProcess
- we use to process for handling heavy cpu task
- step will be similar to thread in asyncio
- ```py
    # cpu intensive task will be handle by process
    import asyncio
    from concurrent.futures import ProcessPoolExecutor

    # encrypt data
    def encrypt(data):
        return f"{data[::-1]}"

    async def main():
        loop = asyncio.get_running_loop()
        with ProcessPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, encrypt, "this_is_password")
            print(result)

    if __name__ == "__main__":
        asyncio.run(main())

    # Ouput
    # drowssap_si_siht

## Example: logger example (async and thread)

- A daemon runs in the background.It kills itself when the main program finishes. othwerwise run forever as per condition we have given

- ```py
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
    ```

## Daemon vs Non-Daemon Threads
- problem : prg may exit before your thread finishes
1. **daemon threads** : they are background threads which automatically shuts down when main prg exits.(usually quiet bg tasks)
    - usage: for non critical bg task (logging , monitoring)
        - Auto-Saves: Writing temporary backup drafts constantly while typing.
            - Word Processor: You keep typing smoothly (Main Thread) while a separate thread quietly auto-saves your file every 10 seconds without making your keyboard lag.
            - Video Game: You play the game at 60 FPS (Main Thread) while a separate thread quietly downloads the next map texture in the background.
        - Heartbeats: Sending a ping every few seconds to show you are online.
        - Metrics: Monitoring system RAM usage for a live dashboard.

    - ```py
        import threading
        import time

        def monitor_tea_temp():
            while True:
                time.sleep(3)
                print("monitoring current temp...")

        t = threading.Thread(target=monitor_tea_temp, daemon=True) # shutdown as main prg exists
        t.start()
        # t.join()  # Blocks the main thread until the specific thread (t) finishes

        print("I am the main prg!")

        # Output
        # I am the main prg!
        ```

2. **Non-daemon threads** : they are background threads that keep on running even after main prg exits.
    - usage : Saving a critical file to disk or finishing a database write.
        - Final Saves: Guaranteeing a file is 100% written to disk before quitting.
        - Clean Closures: Safely closing network connections so data isn't corrupted.
        - Payments: Ensuring a bank transaction completes before the app shuts down.
    - ```py
        import threading
        import time

        def monitor_tea_temp():
            while True:
                time.sleep(3)
                print("monitoring current temp...")

        t = threading.Thread(target=monitor_tea_temp) #keep running after main prg exit
        t.start()

        print("I am the main prg!")
    ```

- Daemon Negation using join: 
    - Setting daemon=True normally allows the program to exit even if the background thread is still running. 
    - However, t.join() completely overrides this behavior by forcing the main thread to stay alive and wait.
    - It only blocks the calling thread (in this case, your main program).
        -  Think of It Like Ordering Food 
            - Without join(): You order food at a counter (start a thread) and immediately walk outside to do other errands (main program continues).
            - With join(): You order food at the counter and stand right there waiting until the food is ready (main program blocks). You are stuck, but the kitchen staff (background thread) is still actively cooking.

###  CODE FLOW (With daemon=True)
- flow 1 **With daemon=True**
1. Load: Python saves the 'monitor_tea_temp' function structure into memory.
2. Setup: Main thread creates the thread object 't' and marks it as daemon.
3. Start: Main thread calls 't.start()', which tells the OS to start the background thread.
4. Split: 
    - Background thread immediately starts running and hits the 3-second sleep.
    - Main thread simultaneously moves down and prints "I am the main prg!".
5. Exit: Main thread finishes its last line of code and stops.
6. Kill: Because daemon=True, Python instantly shuts down the entire program, killing the background thread right in the middle of its sleep.

- flow 2 **ALTERNATE FLOW (If daemon=False)**
    - Steps 1 to 4 are exactly the same.
5. End of Code: Main thread prints "I am the main prg!" and finishes its lines.
6. Kept Alive: Python checks and sees a non-daemon thread is still running. It refuses to close the program and keeps the memory open.
7. Forever Loop: The background thread keeps waking up every 3 seconds, printing, and looping forever. The program never exits on its own.

- flow 2 **(If t.join() is UNCOMMENTED / ACTIVE)**
- Steps 1 to 3 (Load, Setup, and Start) are exactly the same as Flow 1.
4. Block: Instead of moving past, the main thread hits 't.join()' and freezes 
    - completely on that line. It cannot move down to print "I am the main prg!".
5. Loop: The background thread runs completely unblocked in the background. 
    - It wakes up every 3 seconds, prints "monitoring...", and loops forever.
6. Stuck: Because the background loop never ends, 't.join()' never unblocks. 
    - The main thread stays frozen forever, regardless of daemon status.
    - FIX: If t.join(timeout=X) is used with a time limit


###  Apppication of join
- 🛑 Using t.join()
Blocks the main program until the thread is 100% finished.
1. Installers: Waits for file extraction before clicking "Finish".
2. Video Editors: Waits for clip rendering before exporting.
3. Scrapers: Waits for website data before printing reports.

- ⏱️ Using t.join(timeout=X)
Waits briefly but breaks free if the thread lags.
1. Matchmaking: Waits 30 seconds for players, then adds bots.
2. Smart Homes: Waits 3 seconds for bulbs, then shows "Offline".
3. Logins: Waits 5 seconds for database, then shows timeout error.




# Profiling:
to examine which method or coroutine took how much time.
we use builtin module of python cProfile
- python -m cProfile -s time fineame.py
    - need trained eyes to understand it
for debuging u can use these tool
- py-spy (opensource): for profiling 
- vprof : profiling visualization 

## Race Conditons
### What is it?
A race condition happens when two threads try to change the same data at the same time. The data gets messed up because they overwrite each other's work.
### Where it happens
* Bank Apps: Withdrawing money from two places at once might let you take out more than you have.
* Online Shopping: Two people buying the very last item at the exact same second can cause overselling.
* Seat Booking: Two people booking the same movie or flight seat at the same time.
* File Saving: Two programs writing to the same file at once, corrupting the data.


- example of race condtions 
```py
#race conditon
import threading
import time

chai_stock = 0
# c_lock = threading.Lock()

def restock():
    global chai_stock
    for _ in range(100):
        # with c_lock: # Uncomment to fix the race condition
        current = chai_stock # Step 1: Read shared value into local memory
        time.sleep(0.000001) # Step 2: Force pause so other thread reads same stale data
        chai_stock = current + 1 # Step 3: Write back value, overwriting other thread's work

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join() # Wait for both threads to finish

print("chai stock:", chai_stock) # Prints ~100 instead of 200 due to overwrites


```
Here is the complete step-by-step workflow of the code from start to finish:

* Initialization: The main thread creates the global variable chai_stock in memory and sets its value to 0.
* Thread Creation: A list comprehension defines two separate worker threads configured to run the restock function.
* Parallel Launch: The first for loop calls t.start(), spinning up both background threads to run simultaneously.
* Main Thread Pause: The second for loop calls t.join(), forcing the main thread to freeze and wait until both workers finish.
* Worker Execution: Both background threads enter the restock function and begin their respective 100-iteration loops.
* The Interruption (Read): Thread 1 reads the global chai_stock (value 0) into its local current variable.
* The Switch (Sleep): Thread 1 hits time.sleep(), forcing the CPU to pause it and switch over to Thread 2.
* Stale Read: Thread 2 wakes up, reads the exact same unchanged global value (0), and immediately goes to sleep.
* Overlapping Writes: Both threads wake up, calculate 0 + 1, and write 1 back to chai_stock, erasing one thread's contribution.
* Loop Completion: This cycle repeats 100 times, causing dozens of updates to be completely lost.
* Program Termination: Both worker threads exit, unlocking the main thread which prints out the final corrupted total (~100).

------------------------------
Would you like to see how this exact workflow changes step-by-step when the Lock is turned on?

------
Here is the step-by-step workflow with the Lock turned on (with c_lock: uncommented):

* Initialization: The main thread creates the global variable chai_stock = 0 and a shared c_lock = threading.Lock() object.
* Thread Launch: The main thread spins up Thread 1 and Thread 2, then pauses at t.join() to wait for them.
* Lock Acquisition: Thread 1 arrives at with c_lock: first. It successfully acquires (locks) the lock object.
* The Safe Read: Thread 1 reads the current value (0) into its local current variable.
* The Interruption (Sleep): Thread 1 hits time.sleep(). The CPU pauses Thread 1 and tries to switch context to Thread 2.
* The Block: Thread 2 wakes up and tries to execute with c_lock:. Because Thread 1 holds the lock, Thread 2 is blocked and forced to wait.
* The Switch Back: Since Thread 2 cannot proceed, the CPU switches right back to the sleeping Thread 1.
* The Safe Write: Thread 1 wakes up from sleep, calculates 0 + 1, updates chai_stock = 1, and exits the with block (automatically releasing the lock).
* Next Thread Entry: Now that the lock is free, Thread 2 immediately acquires it, reads the updated value (1), and starts its safe cycle.
* Perfect Synchronization: The threads smoothly take turns one after another. No thread can read or write stale data.
* Accurate Completion: Both threads finish all 100 loops without a single collision.
* Final Print: The main thread resumes and prints the perfectly accurate total: exactly 200.

------------------------------
Would you like to see how to handle situations where a thread might get stuck holding a lock forever (deadlocks)?


-----
## Dead Lock
A deadlock in Python is a concurrency failure mode where two or more threads or processes are unable to progress because each is waiting for a resource that the other is holding

Why it Deadlocks?
1. Thread 1 grabs lock_a.
2. Thread 2 grabs lock_b.
3. Because of the sleep, neither thread releases its lock before needing the other's lock.
4. Thread 1 is stuck waiting for lock_b, while Thread 2 is stuck waiting for lock_a



In Python, standard multi-threading does not use an asynchronous event loop. Instead, it relies on the operating system's thread scheduler and Python's Global Interpreter Lock (GIL).
## Why Control Never Returns

* Threads are Blocked: When time.sleep(1) ends, both threads wake up, but they are immediately blocked at the second with statement.
* No Yielding Mechanism: Unlike asynchronous code (asyncio) which actively yields control back to an event loop when waiting, a blocked thread freezes completely and waits for the OS to release the resource.
* Mutual Dependency: task_1 cannot proceed until lock_b is released, and task_2 cannot proceed until lock_a is released. Neither thread can run code to release its current lock.

## The Core Difference: Threads vs. Event Loop

| Feature | Multi-Threading (our Code) | Asyncio (Event Loop) |
|---|---|---|
| Execution | OS manages switching between threads. | Single thread manages execution pauses. |
| Blocking | A blocked thread freezes completely. | A paused task yields control to other tasks. |
| Deadlock Nature | Permanent freeze unless a timeout(lock_b.`acquire(timeout=2)`) is set. | Rare, as tasks must explicitly await. |

