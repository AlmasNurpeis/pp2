import math
from decimal import Decimal


# 1
class Upper:
    def __init__(self):
        pass

    def getString(self) -> str:
        return input()

    def printString(self, string: str):
        print(string.upper())


# 2
class Shape:
    def __init__(self):
        def area() -> float:
            return 0


class Square(Shape):
    def __init__(self, length: float):
        def area() -> float:
            return length * length


# 3
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__(length)
        self.width = width

    def area(self) -> float:
        return self.length * self.width


# 4
class Point:
    def __init__(self, *dimensions):
        self.dimensions = dimensions

    def print_coordinates(self):
        result = ""
        for dimension in self.dimensions:
            result += f"{dimension} "

        print(result)

    def change_coordinates(self, new_dimensions: tuple):
        self.dimensions = new_dimensions

    def compute_distance(self, other) -> float:
        result = 0
        for dimension, other_dimension in zip(self.dimensions, other.dimensions):
            result += (dimension - other_dimension) ** 2

        return math.sqrt(result)


p1 = Point(1, 2, 3)
p2 = Point(1, 1, 1)
print(p1.compute_distance(p2))


# 5
class Account:
    def __init__(self, owner: str, balance):
        self.owner = owner
        self.balance = Decimal(balance)

    def deposit(self, money):
        new_balance: Decimal = self.balance + Decimal(money)
        self.balance = new_balance

    def withdraw(self, money):
        new_balance: Decimal = self.balance - Decimal(money)
        if new_balance < 0:
            print(f"You cannot withdraw {money:.2f}, you only have {self.balance:.2f} on balance!")
            return

        self.balance = new_balance


my_account = Account("Owner", 0)
my_account.deposit(500.7)
my_account.withdraw(500.6)
my_account.withdraw(1234)

my_account.deposit(100)
my_account.withdraw(200)

# 6
numbers: list = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

if_prime = lambda x: all(x % i != 0 for i in range(2, x))
result_it = filter(if_prime, numbers)
result_list = list(result_it)
print(f"Prime numbers: {result_list}")
