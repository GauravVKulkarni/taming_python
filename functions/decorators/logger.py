from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@logger
def candy_function(candy_name, Quality='Good'):
    print(f"This is a {Quality} quality {candy_name} candy.")

candy_function('Chocolate', 'Terrible')