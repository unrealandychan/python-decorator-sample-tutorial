# Static methods are methods that are bound to a class rather than its object.

# TD:DR -> This is to skip self
class Math:
    # Static methods are defined using the @staticmethod decorator. We don't need to pass self or cls to the method.
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def divide(x, y):
        return x / y if y != 0 else ValueError("Cannot divide by zero")

# We don't have Math object, so we don't need to create an object of Math class to call its methods.
print(Math.divide(1, 2))
print(Math.add(1, 2))
print(Math.multiply(1, 2))
print(Math.subtract(1, 2))