def decorator(func):
    def wrapper():
        print('Decorator: Before Function')
        func()
        print('Decorator: After Function') 
    return wrapper

@decorator
def greet():
    print("Namaste Everyone.")
    
greet()
print('Function name :', greet.__name__) #wrapper

# Decorator: Before Function
# Namaste Everyone.
# Decorator: After Function
# Function name : wrapper

## fix for meta data issue
from functools import wraps

def decorator(func):
    @wraps(func)
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