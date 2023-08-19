import random

target_number = random.randint(1, 100)
guess = -1

while guess != target_number:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess < target_number:
        print('Higher')
    elif guess > target_number:
        print('Lower')
    else:
        print('Congratulations! You guessed teh correct number.')
