
from dataclasses import dataclass

# This is the old day way
class Product:
    def __init__(self, name: str, price: float,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def total_cost(self)->float:
        return self.price * self.quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )

@dataclass
class ProductNew:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self)->float:
        return self.price * self.quantity

p1 = Product("Phone", 500, 3)
p2 = ProductNew("Phone", 500, 3)
print(p1)
print(p2)
print(p1.total_cost())
print(p2.total_cost())
print(p1 == p2) # False

# Another example
p1 = ProductNew("Phone", 500, 3)
p2 = ProductNew("Phone", 500, 3)
print(p1 == p2) # True
