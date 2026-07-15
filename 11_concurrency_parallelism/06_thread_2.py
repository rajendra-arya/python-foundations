import threading
import time

def prepare_chai(type_, wait_time):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: ready.")

t1 = threading.Thread(target=prepare_chai, args=("masala", 6))

t2 = threading.Thread(target=prepare_chai, args=("lemon", 3))

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()

print(f"Everything is done in! {end-start:.2f}" )
#this is one process(aka main) having multiple thread, its a one core/cpu only.
