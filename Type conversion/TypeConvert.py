# Type conversion is the process of converting one datatype to another

# Converting integer to float
height = 5.5
newHeight = int(height)
print(newHeight)

# Converting float to integer
age = 13
newAge = float(age)
print(newAge)

# Converting integer to string
num = 9112
num = str(num)
print(num)
print(f"The datatype of num is now {type(num)}")

# Converting a string to a boolean, if th string has some value, 
# it returns true, if there is nothing, it will return False
name = "Reodesu"
name = bool(name)
print(name)