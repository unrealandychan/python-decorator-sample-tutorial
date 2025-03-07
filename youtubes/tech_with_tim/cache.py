import functools

@functools.lru_cache()
def fibonacci(n):
    if n <2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40)) # 102334155