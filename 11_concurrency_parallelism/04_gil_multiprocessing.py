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


# main method error
# - its doesn't cause error in thread
# - as in concurrency they know there entry point 
# RuntimeError
# if u dont use main in the multiprocessing: 
# An attempt has been made to start a new process before the
# current process has finished its bootstrapping phase.
# This probably means that you are not using fork to start your
# child processes and you have forgotten to use the proper idiom
# in the main module:
# - it means u dont have main,which is a freeze support


