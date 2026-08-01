word = "Tanker"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"404, {letter} was not found")
else:
    print(f"There is a/an {letter} in the word")