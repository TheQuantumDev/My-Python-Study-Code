# These are also known as dunder methods (__init__, __str__, __eq__)
# They are automatically called by many of python's built-in operations
# They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_of_pages):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages

    # This gives the string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author} with {self.num_of_pages} pages"
    
    # This helps check the equality of two objects
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # This helps to check if a part of an object is less than the other
    def __lt__(self, other):
        return self.num_of_pages < other.num_of_pages
    
    # This helps to check if a part of an object is greater than the other
    def __gt__(self, other):
        return self.num_of_pages > other.num_of_pages

book1 = Book("C++ made easy", "Ronald Okuk", 200)
book2 = Book("The Minecraft ultimate guide", "Dorinano", 150)
book3 = Book("Gamers united", "Darryl Okuk", 100)
book4 = Book("The GOAT of football", "Notsr7", 350)
book5 = Book("The GOAT of football", "Notsr7", 300)

print(book1)
print(book2)
print(book3)
print(book4 == book5)
print(book5 < book4)
print(book5 > book4)