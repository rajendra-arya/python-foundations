import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled.")

def toast_bun():
    print("Toasting Bun...")
    time.sleep(5)
    print("Done with Bun Toasting.")

# start = time.time()

# boil_milk()
# toast_bun()

# end = time.time()
# print(f"Breakfast is ready in {end-start:.2f} seconds.")

# output
    # Boiling milk...
    # Milk Boiled.
    # Toasting Bun...
    # Done with Bun Toasting.
    # Breakfast is ready in 7.00 seconds.


# by threading 
start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Breakfast is ready in {end-start:.2f} seconds.")
# output
    # Boiling milk...
    # Toasting Bun...
    # Milk Boiled.
    # Done with Bun Toasting.
    # Breakfast is ready in 5.01 seconds.