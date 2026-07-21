import threading
import time

def monitor_tea_temp():
    while True:
        time.sleep(3)
        print("monitoring current temp...")

t = threading.Thread(target=monitor_tea_temp) #keep running after main prg exit
t.start()

print("I am the main prg!")

# Output
# I am the main prg!
# monitoring current temp...
# monitoring current temp...
# monitoring current temp...
# monitoring current temp...


# code flow
# 1. Load: Python saves the 'monitor_tea_temp' function structure into memory.
# 2. Setup: Main thread creates the thread object 't' and marks it as daemon.
# 3. Start: Main thread calls 't.start()', which tells the OS to start the 
#    background thread.
# 4. Split: 
#    - Background thread immediately starts running and hits the 3-second sleep.
#    - Main thread simultaneously moves down and prints "I am the main prg!".
# 5. End of Code: Main thread prints "I am the main prg!" and finishes its lines.
# 6. Kept Alive: Python checks and sees a non-daemon thread is still running. 
#    It refuses to close the program and keeps the memory open.
# 7. Forever Loop: The background thread keeps waking up every 3 seconds, 
#    printing, and looping forever. The program never exits on its own.