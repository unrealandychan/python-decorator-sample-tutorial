# Python Decorators
This is a simple example of how to use decorators in Python. With decorators, you can add functionality to an existing function without modifying it. This is useful when you want to add functionality to a function that you don't have access to modify. Since I learn something from functional programming, I think it's a good idea to share with you.

## What is a decorator?
A decorator is a function that takes another function as an argument and returns a new function. This new function can add some functionality to the original function without modifying it.

## How to use a decorator?
To use a decorator, you need to define a function that takes another function as an argument and returns a new function. You can then use the `@` symbol followed by the name of the decorator function before the definition of the function you want to decorate.

## Higher Order Functions
In Python, functions are first-class objects, which means that you can pass them as arguments to other functions and return them from other functions. Functions that take other functions as arguments or return other functions are called higher-order functions.

## Example
In this example, we define a decorator function called `logger` that adds logging functionality to a function. We then use this decorator to add logging to the `add` function.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args} kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

@logger
def add(a, b):
    return a + b
```

When we call the `add` function, the `logger` decorator will print the function name, arguments, and return value.

## Reference
- [Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python進階技巧 (3) — 神奇又美好的 Decorator ，嗷嗚！](https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-3-%E7%A5%9E%E5%A5%87%E5%8F%88%E7%BE%8E%E5%A5%BD%E7%9A%84-decorator-%E5%97%B7%E5%97%9A-6559edc87bc0)

## Conclusion
Decorators are a powerful feature of Python that allows you to add functionality to existing functions without modifying them. By using decorators, you can keep your code clean and modular, making it easier to maintain and extend in the future.
