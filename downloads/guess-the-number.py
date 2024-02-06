# guess.py

import random

number = random.randint(1, 20)
print('Guess my number between 1 and 20: ', end='')
running = True
tries = 0
while running:
    guess = input()

    if guess.isdigit():
        guess = int(guess)
        if guess > 20 or guess < 1:
            print('Enter a digit between 1 and 20: ', end='')
        else:
            tries += 1
            if guess > number:
                print('It\'s lower than that! Try again: ', end='')
            elif guess < number:
                print('It\'s higher than that! Try again: ', end='')
            else:
                print('Yup! You guessed it! ', end='')
                print(f'It took you {tries} tries to guess it!')
                running = False
    else:
        print('Please enter a digit between 1 and 20: ', end='')
