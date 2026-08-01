from Script2 import fav_drink

def fav_food(food):
    print(f"Your fav food is {food}")

# Only run tis code when running file directly
# else dont run in any other file even when imported by other files
def main():
    print("This is script1")
    fav_drink("Coke")
    print("Bis spater:)")

if __name__ == '__main__':
    main()