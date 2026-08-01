word = "Missile"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a/an {letter} in the word")
else:
    print(f"{letter} is not in the word")