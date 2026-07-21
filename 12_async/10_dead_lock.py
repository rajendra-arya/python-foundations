# dead lock
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def task_1():
    with lock_a:
        print("Task 1 acquired lock a 🔒")
        time.sleep(1)
        with lock_b:
            print("Task 1 acquired lock b 🔒")

def task_2():
    with lock_b:
        print("Task 2 acquired lock b 🔒")
        time.sleep(1)
        with lock_a:
            print("Task 2 acquired lock a 🔒")

t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)

t1.start()
t2.start()

# output
# Task 1 acquired lock a 🔒
# Task 2 acquired lock b 🔒



# dead lock without sleep chances r low
# import threading
# import time

# lock_a = threading.Lock()
# lock_b = threading.Lock()

# def task_1():
#     with lock_a:
#         print("Task 1 acquired lock a 🔒")

#         with lock_b:
#             print("Task 1 acquired lock b 🔒")

# def task_2():
#     with lock_b:
#         print("Task 2 acquired lock b 🔒")

#         with lock_a:
#             print("Task 2 acquired lock a 🔒")

# t1 = threading.Thread(target=task_1)
# t2 = threading.Thread(target=task_2)

# t1.start()
# t2.start()

# Because your code executes sequentially faster than thread switching occurs, the threads often complete one by one before a deadlock can be triggered
# Task 1 acquired lock a 🔒
# Task 1 acquired lock b 🔒
# Task 2 acquired lock b 🔒
# Task 2 acquired lock a 🔒