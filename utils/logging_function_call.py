from math import sqrt
import logging
def function_call_decorator(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"Calling {func.__name__}") # We can use logging.info() instead of logging.debug() to get the same result as the other snippets
        value = func(*args, **kwargs)
        logging.debug(f"Finished {func.__name__}")
        return value
    return wrapper

@function_call_decorator
def is_prime(num:int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

logging.basicConfig(level=logging.DEBUG)
print(is_prime(333))