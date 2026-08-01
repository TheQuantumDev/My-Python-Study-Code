from abc import ABC, abstractmethod
import math

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return math.pow(self.side, 2)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(4), Square(8), Triangle(6, 7)]

for shape in shapes:
    print(f"{shape.area():.2f}cm²")
