print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1,10)

isGuessRight = False # set initial condition

while isGuessRight != True: # if not True, guess the number
    
    guess = input("Guess a number between 1 and 10: ")

    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True # change to True and exit while loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))