import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():                      # Here, you're making sure the user's input is a digit 
    top_of_range = int(top_of_range)            # Here, you're converting the user's string input into an integer

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()

else:
    print('Please type a number next time.')
    quit()
    
random_number = random.randint(0, top_of_range)    # This will generate a random number up to whatever number the user specified
guesses = 0                                         # This is going to keep track of all the user's guesses 

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)            

    else:
        print('Please type a number next time.')
        continue                                    # continue will bring you back to the top of your loop

    if user_guess == random_number:
        print("You got it!")
        break                                       # Once the right number is guessed, the loop will be broken

    elif user_guess > random_number:
        print("Guess a little lower")

    else:
        print("Guess a little higher")
        

print("You got it in", guesses, "guesses")


