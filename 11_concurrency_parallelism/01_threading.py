import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(1)


def brew_chai():
    for i in range(1, 4):
        print(f"\t Brewing chai for #{i}")
        time.sleep(3)

# take_orders()
# brew_chai()

# Taking order for #1 
# Taking order for #2 
# Taking order for #3
#          Brewing chai for #1 
#          Brewing chai for #2 -after 3s
#          Brewing chai for #3 -after 6s



# -----using concurrency
#create threads  - it should have a target
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# invoke thread
order_thread.start()
brew_thread.start()

# multi threading - have to wait for all to perform and complete and then move next
order_thread.join()
brew_thread.join()

print('All orders taken and chai is brewed')


# Taking order for #1
#          Brewing chai for #1 -wait for 3s
# Taking order for #2
# Taking order for #3
#          Brewing chai for #2 - after 3s
#          Brewing chai for #3  - after 6s
# All orders taken and chai is brewed