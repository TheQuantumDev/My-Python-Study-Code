#     MultiThreading is used to perform multiple tasks concurrently
#     (multitasking). It is good for I/O bound tasks like reading files 
#     or fetching data from APIs.
#     First import the threading module
#     Make a thread constructor and pass a target argument
#     Thread(target = my_function)
import threading
import time

def wash_dishes():
    time.sleep(5)
    print("You wash the dishes")

def sweep_the_floor():
    time.sleep(3)
    print("You sweep the floor")

def coding_some_projects():
    time.sleep(10)
    print("You work on some coding projects")

chore1 = threading.Thread(target=wash_dishes)
chore1.start()

chore2 = threading.Thread(target=sweep_the_floor)
chore2.start()

work = threading.Thread(target=coding_some_projects)
work.start()

chore1.join()
chore2.join()
work.join()

print("All chores are complete!")
print("Hurray🎉")