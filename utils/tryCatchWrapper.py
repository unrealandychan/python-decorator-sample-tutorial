import functools
import logging

# This wrapper can simplify the try-catch block in the function
def try_catch_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception occurred {e}")
            logging.error(f"Error on {func.__name__}")
            return
    return wrapper

@try_catch_wrapper
def may_error(num:int) -> int:
    if num < 2:
        raise ValueError("Number is too small")
    return num

logging.basicConfig(level=logging.DEBUG)
for i in range(10):
    result = may_error(i)
    print(result)