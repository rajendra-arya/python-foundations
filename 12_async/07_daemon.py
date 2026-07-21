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


# code flow
# 1. Load: Python saves the 'monitor_tea_temp' function structure into memory.
# 2. Setup: Main thread creates the thread object 't' and marks it as daemon.
# 3. Start: Main thread calls 't.start()', which tells the OS to start the 
#    background thread.
# 4. Split: 
#    - Background thread immediately starts running and hits the 3-second sleep.
#    - Main thread simultaneously moves down and prints "I am the main prg!".
# 5. Exit: Main thread finishes its last line of code and stops.
# 6. Kill: Because daemon=True, Python instantly shuts down the entire program, 
#    killing the background thread right in the middle of its sleep.