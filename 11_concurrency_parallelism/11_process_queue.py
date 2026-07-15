from multiprocessing import Process, Queue , Value

def prepare_chai(queue):
    #add data in queue
    queue.put("Masala Chai is ready.")
    queue.put("Masala Chai is not ready.")


if __name__ == "__main__":
    # generate the queue, it will be passed
    queue = Queue()
    # pass queue obj as argument for storing data
    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    while not queue.empty():
        print(queue.get())


# Output
# Masala Chai is ready.
# Masala Chai is not ready.
    