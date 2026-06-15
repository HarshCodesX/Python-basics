# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer # instead of calling the function directly, we are passing it to the decorator
def example_function(n):
    time.sleep(n)

example_function(2)