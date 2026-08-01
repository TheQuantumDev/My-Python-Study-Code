from Script1 import fav_food

def fav_drink(drink):
    print(f"Your fav drink is {drink}")

# Only run tis code when running file directly
# else dont run in any other file even when imported by other files
def main():
    print("This is script2")
    fav_food("Meat Pie")
    print("Bis Bald:)")

if __name__ == '__main__':
    main()