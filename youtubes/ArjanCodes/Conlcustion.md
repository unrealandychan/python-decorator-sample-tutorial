# Pro and Cons of using decorators

## Pros
- **Code Reusability**: Decorators allow you to add functionality to an existing function without modifying it. This makes your code more modular and reusable.
- **Separation of Concerns**: By using decorators, you can separate the core logic of a function from the additional functionality. This makes your code easier to understand and maintain.
- **Cleaner Code**: Decorators help you keep your code clean and concise by removing repetitive code that would otherwise be scattered throughout your codebase.
- **Easy to Extend**: Decorators make it easy to add new functionality to an existing function without modifying it. This makes it easier to extend your code in the future.

## Cons
- **Complexity**: Decorators can make your code more complex and harder to understand, especially if you have multiple decorators applied to a single function.
- **Performance Overhead**: Decorators can introduce a performance overhead, especially if the decorator function is computationally expensive.
- **Debugging**: Decorators can make it harder to debug your code, as the flow of execution can be more difficult to follow when decorators are involved.
- **Signatures**: Decorators can change the signature of the decorated function, which can make it harder to work with tools that rely on function signatures, such as IDEs and static analysis tools.
- **Order of Execution**: The order in which decorators are applied can affect the behavior of the decorated function, which can be confusing if you are not aware of the order of execution.

## What is function signature?
The function signature is a unique identifier for a function that includes the function name, parameter types, and return type. The function signature is used by the Python interpreter to determine which function to call when a function is invoked.
Example:
```python
def add(a: int, b: int) -> int:
    return a + b
```
In this example, the function signature of the `add` function is `add(int, int) -> int`.

And why decorators can change the function signature?
Decorators can change the function signature by wrapping the original function in a new function that takes different arguments or returns a different value. This can make it harder to work with tools that rely on function signatures, such as IDEs and static analysis tools.
Example:
```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args} kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper
```
In this example, the `logger` decorator changes the function signature of the decorated function by wrapping it in a new function that takes `*args` and `**kwargs` as arguments.
