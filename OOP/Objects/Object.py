class Car:
    def __init__(self, model, year, color, price):
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def drive(self):
        print(f"You drive the {self.color} {self.model}🟢")

    def stop(self):
        print(f"You stop the {self.color} {self.model}🔴")

car1 = Car("CyberTruck", 2077, "Silver", 1000000000)
car2 = Car("Lamborghini", 2025, "Blue", 5000000)

print(f"A {car1.color} {car1.year} {car1.model} worth ${car1.price}")
print(f"A {car2.color} {car2.year} {car2.model} worth ${car2.price}")

car1.drive()
car1.stop()

car2.drive()
car2.stop()