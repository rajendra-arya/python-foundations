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


# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 106
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 200
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 104
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 100
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 100
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 105


    #  with c_lock:
    #         current = chai_stock 
    #         time.sleep(0.000001)
    #         chai_stock = current + 1

#     PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py 
# chai stock: 200
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 200
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 200
# PS E:\AI\rajend\course\python-course> python .\12_async\09_race_conditons.py
# chai stock: 200


#---fix--
# #race conditon
# import threading
# import time

# chai_stock = 0
# c_lock = threading.Lock()

# def restock():
#     global chai_stock
#     for _ in range(100):
#         with c_lock:
#             current = chai_stock 
#             time.sleep(0.000001)
#             chai_stock = current + 1

# threads = [threading.Thread(target=restock) for _ in range(2)]

# for t in threads: t.start()
# for t in threads: t.join()

# print("chai stock:", chai_stock)