# When a child class inherits from more than one parent class

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Prey:
    def panic_and_run(self):
        print("This animal is running away")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.panic_and_run()

hawk.hunt()

fish.hunt()
fish.panic_and_run()