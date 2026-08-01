# When a parent can inherit from another parent

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Prey(Animal):
    def panic_and_run(self):
        print(f"{self.name} is running away")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

rabbit = Rabbit("Rocky")
hawk = Hawk("Tony")
fish = Fish("Fred")

rabbit.panic_and_run()
rabbit.eat()
rabbit.sleep()

hawk.hunt()
hawk.eat()
hawk.sleep()

fish.hunt()
fish.panic_and_run()
fish.eat()
fish.sleep()