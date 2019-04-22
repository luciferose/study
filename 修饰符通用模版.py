from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper