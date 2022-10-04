from functools import wraps 

def trace(func):
    @wraps(func)
    def traced(*args, **kwargs):
        print("calling", func, "with args", *args, "and kwargs", **kwargs)
        return func(*args, **kwargs)
    return traced

@trace
def add(*args):
    """
    add numbers together 
    """
    return sum(args)