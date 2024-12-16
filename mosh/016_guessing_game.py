number = 7
chances = 3
attempts = 0

while attempts < chances:
    guess = float(input(f"Guess: "))
    if guess != number:
        attempts = attempts + 1
        print(f"Wrong! You have {chances - attempts} attempts left")
    elif guess == number:
        print(f"You win!")
        break
else:
    print(f"You loser!")