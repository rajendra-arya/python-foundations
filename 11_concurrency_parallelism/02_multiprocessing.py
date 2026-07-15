from multiprocessing import Process
import time


def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"\tEnds of {name} chai brewing")

if __name__ == "__main__":
    # Create the process instance
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
        ]
    
    # Start all Process
    for p in chai_makers:
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