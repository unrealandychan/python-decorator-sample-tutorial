
from dataclasses import dataclass, field


# Original
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.x == other.x and self.y == other.y

# New
@dataclass
class PointNew:
    x: int
    y: int

p = PointNew(1, 2)
p1 = PointNew(1, 2)
print(p == p1) # True
# Much cleaner ,huh?

## More complicated example

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    sizes:list[str] = field(default_factory=list) # This is how you can set a default value for a list

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

    def add_size(self, size:str):
        self.sizes.append(size)

    def remove_size(self, size:str):
        self.sizes.remove(size)

## Inheritance
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        self.width = self.side
        self.height = self.side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

sq1 = Square(5)
print(sq1.side)
print(sq1.width)
print(sq1.area())

## Another example
@dataclass
class Animal:
    name:str
    species:str

@dataclass
class Dog(Animal):
    breed:str

@dataclass
class Cat(Animal):
    breed:str

dog1 = Dog("Buddy", "Dog", "Golden Retriever")
cat1 = Cat("Kitty", "Cat", "Siamese")
print(dog1)
print(cat1)