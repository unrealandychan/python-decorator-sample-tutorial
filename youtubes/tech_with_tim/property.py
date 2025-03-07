import math

# This show the case of @property decorator
class Circle:
    def __init__(self, radius:float):
        self._radius = radius # _radius is a private variable

    # @property decorator is used to define a method that can be accessed as an attribute
    @property
    def radius(self) -> float:
        return self._radius

    # @property.setter is used to define a setter method for the property
    @radius.setter
    def radius(self, value:float) -> None:
        """Set the radius of the circle"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # Similarly, we can define a property for diameter and area
    @property
    def diameter(self) -> float:
        return 2 * self._radius

    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)
print(c.diameter)
print(c.area)
c.radius = 10
print(c.radius)
print(c.diameter)
print(c.area)