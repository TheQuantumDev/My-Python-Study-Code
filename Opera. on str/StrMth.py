name = input("Enter full name: ")

# .find() gives the index of a character if it is found
result = name.find("R")
print(result)

# .rfind() gives the index of a character if found from the back
result2 = name.rfind("o")
print(result2)

# .capitalize() makes the first letter uppercase
result3 = name.capitalize()
print(result3)

# .upper() makes a string uppercase
result4 = name.upper()
print(result4)

# .lower() makes a string lowercase
result5 = name.lower()
print(result5)

# .isdigit() checks if something only contains digits
result6 = name.isdigit()
print(result6)

# .isalpha() checks if something only contains alphabets *no space*
result6 = name.isalpha()
print(result6)

# .count() counts how much a specific character is
result7 = name.count("o")
print(result7)

# .replace() replaces a character with another
result8 = name.replace("o", "a")
print(result8)