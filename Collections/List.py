cars = ["Camry", "Ford", "Bugatti", "CyberTruck"]

# The empty print statements are to give some spacing in the terminal

cars[0] = "BMW"

print(cars)

print()                                             

print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])

print()

for car in cars:
    print(car, end=" ")

print()
print()

print(f"length of list is {len(cars)} elements long")

print()

print("Tesla" in cars)

print()

print("Add(append) Monster Truck to the end of list")
cars.append("Monster Truck")
print(cars)

print()

print("Remove Ford")
cars.remove("Ford")
print(cars)

print()

print("Insert Volkswagen at index of 0")
cars.insert(0, "Volkswagen")
print(cars)

print()

print("Sorted list")
cars.sort()
print(cars)

print()

print("Reversed list")
cars.reverse()
print(cars)

print()

print("Index of BMW")
print(cars.index("BMW"))

print()

print("Cleared list")
cars.clear()
print(cars)
