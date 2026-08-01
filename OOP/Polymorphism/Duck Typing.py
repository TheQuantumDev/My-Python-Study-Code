# This achievable if an object has minimum necessary attributes/methods
# Think of it as "If it looks like a duck, quacks like a duck, it must be a duck🦆"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("The dog goes *woof*🐶")

class Cat(Animal):
    def speak(self):
        print("The cat goes *meow*🐱")

class Car():
    alive = False
    def speak(self):
        print("The car goes *beep*🚘")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(f"Is alive: {animal.alive}")