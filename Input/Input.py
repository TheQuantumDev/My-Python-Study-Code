name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
is_student = bool(input("Are you ar student(True or False): "))

print("Hello", name)
print("You are", age, "years old")
print(f"You are {height}cm tall")

if(is_student):
    print("You are a student")
else:
    print("You are not a student")