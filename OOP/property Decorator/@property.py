# @property is a decorator used to define a method as a property
# It can be accessed like an attribute
# Benefit: Add additional logic when read, write, or delete attributes
# It gives you getter, setter and deleter methods

class Rectangle:
    def __init__(self, width, height):
        # The _ tells one that these attributes are private
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("The width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("The height has been deleted")

rectangle = Rectangle(4, 5)

rectangle.width = 20
rectangle.height = 10

del rectangle.width
del rectangle.height