# With this game, the computer knows a random number that we're trying to guess

import random

def guess(x):
    random_number = random.randint(1,x) #This tells the computer to pick a number between 1 and x
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('Sorry, please guess again. Too low')
        elif guess > random_number:
            print('Sorry, please guess again. Too high')

    print(f'Yay, congratulations. You have guessed the number {random_number} correctly!')

guess(10)

# Now we're trying to get the computer to guess a number that we made up 

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could also be high b/c low = high
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number {guess} correctly!')

computer_guess(10)







