# Generators 
- any function which contains yield keyword is a generator, it returns generator object.
- used for saving memory
- gives one value at a time
- syntax is similar to func just **it should contains yield** keyword.
- yield : 
    - yield means pause and give 
    - it pause and resume the execution of a function
- The Key Differences
    - `return`: Ends the function. Destroys all local variables. STOP
    - `yield`: Pauses the function. Saves the current state for later. PAUSE
   
    - ```py
        def gen_example():
            yield "Cup 1"  #Pauses execution and sends "Cup 1" out to the caller
            yield "Cup 2"
            yield "Cup 3"
        
        print(gen_example())   #To get the words, you must use a loop or next().
        
        # if order = ...: Resumes function and saves incoming data.
        ```
    - Sending OUT: `yield "Cup 1"` pauses and sends text to you.
    - Receiving IN: `order = yield` pauses, waits for you to send data back, and saves it in order.

- `next(variable)` : runs a paused generator until it hits the next yield and grabs its value.
    - `next(gen_example())` fetches one yield item at a time
- ```py
    # normal function
    def func_example():
        return ["Cup 1", "Cup 2","Cup 3"] 
    print(func_example())  #stores in memory
    #['Cup 1', 'Cup 2', 'Cup 3']


    # generators
    def gen_example():
        yield "Cup 1"
        yield "Cup 2"
        yield "Cup 3"

    print(gen_example())  # gives refrence of object in the memory
    # <generator object gen_example at 0x0000023381EA5BC0>


    print(next(gen_example())) #Cup 1
    print(next(gen_example())) #Cup 1

    cups = gen_example()  
    print(cups) #<generator object gen_example at 0x000001B0C03E5C70>


    print(next(cups)) #Cup 1
    print(next(cups)) #Cup 2 #as long as same var gonna call it will run 1,2,3....
    print(next(cups)) #Cup 3
    print(next(cups)) #Error : StopIteration: error exceeded the total yield
    ```

## Infinite Generators
```py
    #infinte generators
    def infinite_gen_example():
        count = 1
        while True:
            yield f"Refill {count}"
            count+=1

    user1 = infinite_gen_example() 
    print(user1) #<generator object infinite_gen_example at 0x0000015524D36680>

    user2 = infinite_gen_example()
    print(user2) #<generator object infinite_gen_example at 0x0000015524D35E40>

    for _ in range(5):
        print(next(user1))

    for _ in range(5):
        print(next(user2))

    # ouput
    # Refill 1
    # Refill 2
    # Refill 3
    # Refill 4
    # Refill 5
    # Refill 1
    # Refill 2
    # Refill 3
    # Refill 4
    # Refill 5

```

## Send value to Generators

1. `yield` : 
    - it is also used for getting the vlaue from outside using `obj.send('value')` method.
    - it pauses the prg until it gets the value
    - helps in controlling the infinite loop(like while True)
    - Note: A new generator starts at line 0 before any code executes. It must run until it reaches a yield assignment statement before a variable exists to store your data.
    
    
- Example: 
    ```py
    def chai_customer():  # <--- LINE 0 (Created, but paused right here)
    print("Welcome!, What Tea would you like to have?")
    order = yield #wait until it gets the value
    while True:
        print(f'Preparing {order}.')
        order = yield #wait until get the value

    stall = chai_customer()
    next(stall) #starting the generator

    stall.send('Masala Chai')
    stall.send('Lemon Tea')
    ```

## yield from and close
1. `yield from`
    - yield from somewhere else
    - u won't need next() in it
    - ```py
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

        stall = full_menu()
        print(next(stall)) # Lemon chai
        print(next(stall)) # Masala Tea
        print(next(stall)) # Ginger Tea
        print(next(stall)) # Match

        for chai in stall:
            print(chai)
        #Ouput
        # Lemon chai
        # Masala Tea
        # Ginger Tea
        # Matcha
        # Oolang
        ```

2. close()
    - to close your genertor, i.e a cleanup process
    - it gracefully cleans up your memory.
    - so no memory leak, no memory crashes, tons of advantage
    -  it automatically does as well but its good practice to write at the end
    ```py
        def chai_stall():
        try:
            while True:
                order = yield "Waiting for chai order" 
                #step1 -> yield "text...": Pauses function and sends text out.
                #step2 -> order = ...: Resumes function and saves incoming data.
                print(order)
        except:
            print("Stall closed, No more chai.")


        stall = chai_stall()
        print(next(stall))
        print(stall.send('masala'))
        stall.close() #trigger a generator exit method which cleans up the memory

        # print("--- Script is still running here ---")

        #Ouput (when stall.close() before the last line)
            #Waiting for chai order
            #masala
            #Waiting for chai order
            #Stall closed, No more chai.
            #--- Script is still running here ---

        #output when stall.close() not present #Garbage Collection
            #Waiting for chai order
            #masala
            #Waiting for chai order
            #--- Script is still running here ---
            #Stall closed, No more chai.

    ```
    - yield "...": Pauses function and sends data 
    - out.order = ...: Resumes function and saves data sent in.
    - GeneratorExit: Exception injected when the script ends or .close() is called.
    - Garbage Collection: Python automatically destroys the generator at script end, triggering the except: block.


- summary till now 
    1. `yield` : pause and resume execution of a function, 
        - its the main thing responsible for converting function into generators
    2. `next()` : manually getting the next value which generator gonna yeild at us.
    3. `send()` : 
        - send data into the generator
        - next() must run first to advance execution to the yield statement so the variable exists in memory to receive your data.
    4. `yield from` : 
        - getting from another generator 
        - deligate the sub generator for some task
    5. `close()` : 
        - stops the generators for cleaning up the memory gracefully
        - python closes the generator automatically when whole script finishes running.



