# Keyword arguments are arguments preceded with an identifier
# It helps with readability
# Order of arguments don't matter

def greet(greeting, title, first_name, last_name):
    print(f"{greeting} {title}.{first_name} {last_name}")

greet(greeting="Hello", title="Mr", first_name="Dori", last_name="Nano")

print()

for i in range(1, 11):
    print(i, end=" ")

print()
print()

print("1", "2", "3", "4", "5", sep="-")