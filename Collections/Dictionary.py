student = {"name": "Reodesu", "age": 14, "height": 150.5, "is_student": True}

print(student)

print()

# Get value from key
print(student.get("height"))

print()

# Update dictionary
student.update({"Gender": "M"})
print(student)

print()

# Remove a key
student.pop("is_student")
print(student)

print()

# Remove last key
student.popitem()
print(student)

print()

# Get all keys but not values
keys = student.keys()
print(keys)

print()

# Get all values but not keys
values = student.values()
print(values)

print()

# Items of dictionary (kays and values)
items = student.items()
print(items)

print()

# Iterate over keys and values
for key in student.keys():
    print(key)

print()

for value in student.values():
    print(value)

print()

for key, value in student.items():
    print(f"{key}: {value}")

print()

# Clear the dictionary
student.clear()
print(student)