import asyncio 

async def brew_chai(): # define coroutine
    await asyncio.sleep(3) # pauses code without blocking the event loop
    print("Chai is ready.")

asyncio.run(brew_chai())

# Output:
# Chai is ready.(prints after 3 seconds)

#------------------------------------------------------
#  Here is the step-by-step journey of your code, tracking exactly what happens from the moment you hit run until the program finishes.
# ## Phase 1: Registration (Time: 0.00s)

# * The Script Starts: Python reads your file and loads the asyncio module into memory.
# * Coroutine Definition: Python registers brew_chai as an asynchronous function. It does not run the code inside yet; it just creates a blueprint. [1] 

# ## Phase 2: Ignition (Time: 0.00s)

# * asyncio.run() is Called: Python initializes a fresh, hidden control center called the Event Loop.
# * Entering the Function: The Event Loop takes control and triggers the brew_chai() function. [2] 

# ## Phase 3: The Pause (Time: 0.00s to 3.00s)

# * Hitting await: The code encounters await asyncio.sleep(3).
# * Yielding Control: The await keyword tells Python to temporarily pause brew_chai.
# * The Countdown: Control goes back to the Event Loop. The loop puts brew_chai on a waiting list for exactly 3 seconds. Because this is asynchronous, the main thread of your computer is not blocked; the loop simply waits for the timer to alarm. [3] 

# ## Phase 4: Waking Up (Time: 3.00s)

# * Timer Ends: After 3 seconds, the Event Loop sees that the countdown is finished.
# * Resuming execution: The Event Loop wakes up brew_chai right where it left off. [4] 

# ## Phase 5: Completion (Time: 3.01s)

# * Printing Output: The code moves to the next line and prints "Chai is ready." to your terminal.
# * Shutdown: The function returns None. The Event Loop sees no other tasks left to do, shuts itself down safely, and the script exits. [5] 

# ------------------------------
