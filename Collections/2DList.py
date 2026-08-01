groceries = [["Apple", "Orange", "Banana", "StrawBerry"],
            ["Tomato", "Cabbage", "Potato", "Carrot"],
            ["Chicken", "Beef", "Suya", "Fish"]]
print(groceries)

print()

print(groceries[0][0])
print(groceries[1][1])
print(groceries[2][2])

print()

for grocery in groceries:
    for food in grocery:
        print(food, end = " ")
    print()