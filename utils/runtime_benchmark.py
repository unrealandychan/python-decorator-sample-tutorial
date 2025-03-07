import functools
from time import perf_counter
from typing import Any, Callable
from math import sqrt
import logging

def benchmark_decorator(func:Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time:.2f} seconds.")
        return value
    return wrapper

# Example : Count prime numbers
def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True

@benchmark_decorator
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count

# Example: Fibonacci

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@functools.lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# The reason why we can not directly use benchmark on fibonacci is because the function is recursive and the benchmark will be called multiple times
# This will cause the benchmark to be called multiple times and the time will be added up.
# To solve this, we can use the lru_cache from functools to cache the result of the function
@benchmark_decorator
def do_fibonacci(n: int) -> int:
    return fibonacci(n)

@benchmark_decorator
def do_fibonacci_cached(n: int) -> int:
    return fibonacci_cached(n)

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = count_prime_numbers(100000)
    print("Number of prime numbers:", value)

    value = do_fibonacci(40)
    print("Fibonacci(35):", value)

    value = do_fibonacci_cached(40)
    print("Fibonacci(35) with caching:", value)

if __name__ == "__main__":
    main()