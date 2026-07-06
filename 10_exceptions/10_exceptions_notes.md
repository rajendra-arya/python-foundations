# Exceptions
- it's the inevitable situations where our program might crash
- example : 
    - KeyError(dict key error), IndexError, ValueError, ZeroDivisionError(unlike math computer will throw error instead of infinit), NameError(undefined var), TypeError
- handling these exceptions is called exceptions handling.

## Handling with `.get()` method
- It is a dictionary method designed specifically to prevent KeyError exceptions when looking up keys.
- Instead of crashing with a KeyError, `.get()` safely returns `None` if the key does not exist or returns the msg.
- second argument serve as a custom default message if the item isn't on the menu.
- Use .get() when you want a safe, crash-free way to query a dictionary for a key that might be missing. 
- For all other types of errors, you must still use `try...except`
- `print(chai_menu.get("elaichi","Doesn't Exists"))`

## Handling with `try except finally`
- it helps in handling the exceptions gracefully without crashing the program
- try : contains syntax which has potenital of causing error
- except: runs when a error is caught.
    - its also know as caught in other lang
    - u can define exact error, custom made error or jst leave it blank after except.
- finally: runs at the very end, it's the last stament of the prg.
    - eg. cleaning memmory code can be included here, like to closing connection etc.

    ```py
    chai_menu = {'masala':30,'ginger':40}

    # chai_menu["elaichi"] # will cause error and stop the prg(Except)

    # handling with try catch
    try:
        chai_menu["elaichi"]  # error causing code
    except KeyError: #catches the error
        print("Key doesn't exists")

    print("namaste") #runs the prg smoothly while handling error

    #output
        # Key doesn't exists
        # namaste

    # handling with .get() method
    print(chai_menu.get("elaichi","Doesn't Exists"))
    # output - Doesn't Exists
    ```

- Complex example : try catch finally
    ```py
    def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai order...")
        if flavour == 'unknown': #error prone condition
            raise ValueError("Sorry! Flavour Not Avaiable") #raising error
    except ValueError as e: # Handle invalid flavour
        print(f"Error : {e}")
    else:   # run only if no error # notice the identation: its part of try and except now
        print(f"{flavour} Chai is Served.")
    finally: #run always at the end
        print('Next Order Please!\n')


    serve_chai('masala') # runs smoothly
    # try -> if condition fails -> else -> finally

    ## Output
    # masala Chai is Served.
    # Next Order Please!

    serve_chai('unknown') # throws error and handles error
    # try -> if condition true -> raise error -> catches by except -> finally 
    
    ## Output
    # Preparing unknown chai order...
    # Error : Sorry! Flavour Not Avaiable
    # Next Order Please!
    ```



## catching multiple exceptions
- operator overloading : 10*'two' (2 datatype mismatch) python prints the string 10 times.
-  for fixing operator overloading we can do two thing 
    1. Explicit Type Conversion: convert the quantity(if itd number) using `int(quantity)`
    2. Explicit Type Checking : check the quantity is int using type checking methods and then raise type error. 
        -  `isinstance(quantity, int)`:  Checks if the variable is an integer or a child of an integer class (flexible checking).(Recommended)
        - `type(qunatity)` : Checks if the variable is an exact match for a pure integer, ignoring any family tree (strict checking).
        
-  ```py

    def process_order(item, quantity):
        try:
            if not isinstance(quantity,int):
                raise TypeError
            
            price = {"masala":20}[item] #dict[item]: it will check if item exists as the key
            cost = price * quantity 
            print(f"Total cost is {cost}. Thank you!")
        except KeyError:
            print(f"Sorry {item} Chai is not on menu.") 
        except TypeError: #if mismatch of type
            print(f"Quantity {quantity} must be in number.")
        
    process_order("ginger",2)  #Sorry ginger Chai is not on menu.
    process_order("masala",'a') #Quantity a must be in number.
    process_order("masala",4) #Total cost is 80. Thank you!

    ```


## Raise your own errors :
- Raise our own exceptions by using `raise` with errortype.
- `raise ValueError('msg')`
- ```py
    # raise your own errors/exceptions
    def brew_chai(flavour):
        if flavour not in ["masala","ginger","elaichi"]:
            raise ValueError(f"{flavour}: Not Supported Value.")
        print(f"Brewing {flavour} chai...") #if no error it will execute

    brew_chai("ginge")
    
    #Output
    # Traceback (most recent call last):
    #   File "04_custom_exceptions.py", line 7, in <module>
    #     brew_chai("ginge")
    #     ~~~~~~~~~^^^^^^^^^
    #   File "04_custom_exceptions.py", line 4, in brew_chai
    #     raise ValueError(f"{flavour}: Not Supported Value.")
    # ValueError: ginge: Not Supported Value.
    ```


## Creating custom exceptions : 
- we inherit the `Exception` class to create our own custom exception and overide it.
- `class CustomException(Exception):`
    `pass`
- it's used to handle program gracefully, its useful in debugging as well.
- its how custom error happens in libraries, frameworks like fast api, pjango and etc (check spelling)
- ```py
    # creating custom exception
    class OutOfIngreidents(Exception):
        pass

    def make_chai(sugar, milk):
        if sugar==0 or milk==0:
            raise OutOfIngreidents(f'Missing Milk or Sugar')
        print('Preparing Chai...')

    make_chai(1,1) # Preparing Chai...

    make_chai(1,0)

    # Traceback (most recent call last):
    #   File "05_custom_exception_2.py", line 9, in <module>
    #     chai(1,0)
    #     ~~~~^^^^^
    #   File "05_custom_exception_2.py", line 6, in chai
    #     raise OutOfIngreidents(f'Missing Milk or Sugar')
    # OutOfIngreidents: Missing Milk or Sugar

    ```



## Mini Prj
- use case in billing order
-   ```py
        class InvalidChaiError(Exception): pass

        def bill(flavour, cups):
        menu = {"masala":28, "ginger":40}
        try:
        if flavour not in menu:
            raise InvalidChaiError(f"Sorry!, {flavour} Chai is not Available.")
        if not isinstance(cups, int):
            raise TypeError("Sorry! Number of cups must be integer.")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} {flavour} chai is ₹{total}")
        except Exception as e:
        print(e)
        finally:
        print("Thank you for visiting! Have a nice day!\n")

        bill("masala",4)
        # Your bill for 4 masala chai is ₹112
        # Thank you for visiting! Have a nice day!


        bill("masal",4)
        # Sorry!, masal Chai is not Available.
        # Thank you for visiting! Have a nice day!

        bill("masala","sds")
        # Sorry! Number of cups must be integer.
        # Thank you for visiting! Have a nice day!
    ```



## File Handling with `try` `except` and `with`
- The process of handling a file is sensitive as the file opens in memmory, it can lead to issue if it left opened and prg crashed or file gets crashed and cause error.
- We wrap this operation in try catch for graceful error handling.
- We can handle file using 2 way:
1. python inbuild methods - open , with
    - a. Traditional way
        - we explicitly write code for closing the file from memmory
        - ```py
            # Traditional way
            file = open("order.txt", "w")   #opens file or create if not exists and give ref to the var
                                            #its opens file in memmory which can cause errors
            try:   
                file.write("Masala Chai -- 2 cups") # write on that file (its error prone syntax)
            finally:
                file.close #close and remove the file from the memmory
            
            # Output: it will also create a file with it's contents
        ```
    - b. Modern way
        - ```py
            with open("order.txt", "w") as file: #open the file in write mode give ref to var file.
                file.write("Ginger Tea -- 4 cups") # write on that file
            
            # Output: it will also create a file with it's contents
            ```
        - with wraps everything in try catch
            - it contains all try finally inside only and calls it calls enter and exit dunder automatically.
        - file invoke all the dunders automatically without explicitly mentioning it - 
            1. file.__enter__() - responsible for loading in memory , appending n all
            2. file.__exit__() - responsible for removing it out of memory, bts when do file.close() this dunder is called ther as well



2. External libraries - pandas, pillow, etc
    - for txt format python is good enough but for other files like binary, csv etc u should not be handling it with raw python.
    - There are library like pillow , pandas(csv) and others 

---



