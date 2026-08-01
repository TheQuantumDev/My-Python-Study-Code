import random

# Random integers
num = random.randint(1, 10)
print(num)

print()

# Random floating numbers between 0 and 1
num2 = random.random()
print(num2)

print()

# Random choices
options = ["👊", "📃", "✂"]
choice = random.choice(options)
print(choice)

print()

# Shuffle something 
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J", "A"]
shuffle = random.shuffle(cards)
print(cards)