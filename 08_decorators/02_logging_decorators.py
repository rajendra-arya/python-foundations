from functools import wraps

def log_activity(func):
    wraps(func)
    def wrapper(*args, **kwargs): #passing argument and keyword arguments 
        print(f"🚀 Calling : {func.__name__}")

        result = func(*args, **kwargs)

        print(f"✅ Finished : {func.__name__}")
        return result
    return wrapper #we dont call just return the wrapper

@log_activity
def brew_chai(type, milk='no'):
    print(f"Brewing {type} chai. Milk status: {milk}.")

brew_chai('Masala','yes')

