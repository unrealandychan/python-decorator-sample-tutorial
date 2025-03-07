## In Python, function are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).
## This opens up a lot of possibilities for cleaner, more readable code.
# Example 1: Functions as arguments
import functools

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))

## Inner Functions
## It’s possible to define functions inside other functions. Such functions are called inner functions.
def parent():
    print("Printing from the parent() function")

    def first_child():
        return "Printing from the first_child() function"

    def second_child():
        return "Printing from the second_child() function"

    print(first_child())
    print(second_child())

## Syntax Sugar
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

## Decorators with Arguments
def do_twice(func):
    # *args and **kwargs allow the wrapper to accept any arbitrary number of positional and keyword arguments.
    # Explanation: https://realpython.com/python-kwargs-and-args/
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World")

## Decorators with Arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("4 times")

## Creating Decorators With Optional Arguments
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat(num_times=3)
def greet_3_times(name):
    print(f"Hello {name}")

greet("3 times")

@repeat
def say_whee():
    print("Default!")

greet_3_times("World")
say_whee()
