# This is used in a child class to call methods from a parent class

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="Red", is_filled=True, radius=200)
square = Square(color="Blue", is_filled=False, width=150)
triangle = Triangle(color="Yellow", is_filled=True, width=100, height=150)

print(f"The circle is color {circle.color}, it's filled? {circle.is_filled} and it has a radius of {circle.radius}cm")

print(f"The square is color {square.color}, it's filled? {square.is_filled} and it has a width of {square.width}cm")

print(f"The triangle is color {triangle.color}, it's filled? {triangle.is_filled} and it has a width of {triangle.width}cm and a height of {triangle.height}cm")