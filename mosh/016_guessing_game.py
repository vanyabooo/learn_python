import random

while True:  # Цикл, чтобы продолжать просить ввод до правильного числа
    max_number = int(input(f'Введите макисмальное число которое будет загадано: '))

    if max_number <= 1:
        print(f"Эээ братан давай побольше число сделай да")
    else:
        chances = 3
        random_number = random.randint(1, max_number-1)
        attempts = 0

        while attempts < chances:
            guess = int(input(f"Guess: "))
            if guess != random_number:
                attempts += 1
                print(f"Wrong! You have {chances - attempts} attempts left")
            elif guess == random_number:
                print(f"You win!")
                break
        else:
            print(f"You loser!")
        break