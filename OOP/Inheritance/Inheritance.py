class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("The dog goes woof🐶")

class Cat(Animal):
    def speak(self):
        print("The cat goes meow🐱")

class Mouse(Animal):
    def speak(self):
        print("The mouse goes squeak🐭")

dog = Dog("Spike")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print()

print(f"{dog.name} is alive {dog.is_alive}")
dog.eat()
dog.sleep()
dog.speak()

print()

print(f"{cat.name} is alive {cat.is_alive}")
cat.eat()
cat.sleep()
cat.speak()

print()

print(f"{mouse.name} is alive {mouse.is_alive}")
mouse.eat()
mouse.sleep()
mouse.speak()