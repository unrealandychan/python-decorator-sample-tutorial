import logging
from math import sqrt
from time import perf_counter
from typing import Callable


# Using function decorators and syntax sugar to achieve the same result as the object-oriented approach
# This is a more Pythonic way of writing decorators

def logging_decorator(func:Callable[..., int]) -> Callable[..., int]:
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return value
    return wrapper

def benchmark_decorator(func:Callable[[int], int]) -> Callable[[int], int]:
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time:.2f} seconds.")
        return value
    return wrapper

def is_prime(num:int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

@logging_decorator
@benchmark_decorator
def count_prime_numbers(upper_bound:int) -> int:
    count = 0
    for num in range(upper_bound):
        if is_prime(num):
            count += 1
    return count

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = count_prime_numbers(100000)
    print("Number of prime numbers:", value)

if __name__ == "__main__":
    main()