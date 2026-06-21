def local_chai():
    yield 'Lemon chai'
    yield 'Masala Tea'
    yield 'Ginger Tea'

def imported_chai():
    yield 'Matcha'
    yield 'Oolong'

def full_menu(): #generator function
    yield from local_chai()
    yield from imported_chai()

# stall = full_menu()
# print(next(stall)) # Lemon chai
# print(next(stall)) # Masala Tea
# print(next(stall)) # Ginger Tea
# print(next(stall)) # Match

# for chai in stall:
#     print(chai)
#Ouput
# Lemon chai
# Masala Tea
# Ginger Tea
# Matcha
# Oolang


### close ------ for closing genertors

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order" #yield "text...": Pauses function and sends text out. order = ...: Resumes function and saves incoming data.
            print(order)
    except:
        print("Stall closed, No more chai.")


stall = chai_stall()
print(next(stall))
print(stall.send('masala'))
stall.close() #trigger a generator exit method which cleans up the memory

print("--- Script is still running here ---")


# yield "...": Pauses function and sends data 
# out.order = ...: Resumes function and saves data sent in.
# GeneratorExit: Exception injected when the script ends or .close() is called.
# Garbage Collection: Python automatically destroys the generator at script end, triggering the except: block.