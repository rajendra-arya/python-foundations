# Decorators
- primary purpose is for decorations, like sprinkling something on top
- act as a "syntactic sugar"
- its just a wrapper around your function
- concept :
    ```py
    def my_decorator(func):           # 1. drops the original function HERE.
        def wrapper(*args, **kwargs): # 2. drops the func arguments here when called, u can leave it empty too.
            
            # [ Run Before ]          # 3. Your custom "before" code goes here.
            
            func(*args, **kwargs)     # 4. You call the original function using variables(func, args) from 1 & 2.
            
            # [ Run After ]           # 5. Your custom "after" code goes here.
            
        return wrapper                # 6. Returns the wrapper to replace the original function.
    ```
- @decorator_name : whatever is on next line will be wrapped up by this decorator
- use : to decorate(adding wrapper around) the function we need to call the decorator (@decorator_name) just above our function
- by default the func name will be modified as wrapper
- Rule 1: The outermost function (my_decorator) always takes only the function (func).
- Rule 2: The inner function (wrapper) always takes only the arguments (*args, **kwargs) that belong to the function being decorated.

- example:
    - ```py
        def my_decorator(func):  #Receives the function here
        def wrapper(): #  Receives arguments here (even if empty)
            print('Decorator: Before Function')
            func()
            print('Decorator: After Function') 
        return wrapper

        @my_decorator
        def greet():
            print("Namaste Everyone.")
            
        greet()
        print('Function name :', greet.__name__) #wrapper

        # Decorator: Before Function
        # Namaste Everyone.
        # Decorator: After Function
        # Function name : wrapper
        
    ```
- meta data issue from decorator & fix : 
    - alot of meta data of our function is modified by the wrapper
        - your_function.__name__ : will print wrapper name
    - fix:  we will use `functools` library and import `wraps`
        - to preserve the meta data
        - `from functools import wraps`
            - `decor @wraps(func)`
            - `your_function.__name__`: will print function name
    - example:
        ```py
        from functools import wraps

        def decorator(func):
            @wraps(func) #keeps the orignal func name
            def wrapper():
                print('Decorator: Before Function')
                func()
                print('Decorator: After Function') 
            return wrapper

        @decorator
        def greet():
            print("Namaste Everyone.")
            
        greet()
        print('Function name :', greet.__name__) #greet

        # Decorator: Before Function
        # Namaste Everyone.
        # Decorator: After Function
        # Function name : greet

        ```

## use case : logging activity
- this is kinda how decorators used for logging
- code : 
    ```py
        from functools import wraps

        def logging_activity(func):
            wraps(func)
            def wrapper(*args, **kwargs): #passing argument and keyword arguments 
                print(f"🚀 Calling : {func.__name__}")

                result = func(*args, **kwargs)

                print(f"✅ Finished : {func.__name__}")
                return result
            return wrapper #we dont call just return the wrapper

        @logging_activity
        def brew_chai(type, milk='no'):
            print(f"Brewing {type} chai. Milk status: {milk}.")

        brew_chai('Masala','yes')
    # Ouput
    🚀 Calling : brew_chai
    Brewing Masala chai. Milk status: no.
    ✅ Finished : brew_chai
    
    ```

## use case : authentation
- Python Implicit Returns: Every function in Python returns None unless a return keyword is used.
- recommendation(): explicitly use return , something for false conditon to avoid error(helpful in older py version)
    - We use return None to explicitly signal that a function intentionally ended without a valid result
    - inshort is makes prg foolprrof
- ```py
    from functools import wraps

    def require_admin(func):
        wraps(func)
        def wrapper(userrole):  # The PARAMETER goes here
            if(userrole != 'admin'):
                print('Access denied: Admins only')
                return None  # makes prg foolprrof
            else:
                return func(userrole) 
        return wrapper

    @require_admin
    def access_inventory(role):
        print('Access granted to Inventory.')

    access_inventory('user') #Access denied: Admins only
    access_inventory('admin') #Access granted to Inventory.



```
