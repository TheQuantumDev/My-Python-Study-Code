# An exception is an event that interrupts the normal flow of a program
# E.g -> ZeroDivisionError, TypeError, ValueError, etc
# 1. try, 2. except, 3. finally

try:
    num = int(input("Enter a number to be divided by 1: "))
    print(f"The ans is: {1 / num:.2f}")

except ZeroDivisionError:
    print("You can't divide by zero idiot🥴")

except ValueError:
    print("Only enter a number pls")

except Exception:
    print("Something went wrong🤔")