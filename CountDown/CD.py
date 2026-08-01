import time

CD_from = int(input("How many seconds to count down from: "))

for i in reversed(range(1, CD_from + 1)):
    print(i)
    time.sleep(1)
print("Missile launch🚀")