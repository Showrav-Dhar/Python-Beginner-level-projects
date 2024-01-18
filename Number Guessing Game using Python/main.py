# Number Guessing Game using Python To create a guessing game,
# we need to write a program to select a random number between 1 and 10.
# To give hints to the user,
# we can use conditional statements to tell the user
# if the guessed number is smaller, greater than or equal to the randomly selected number.
# the game will run until user makes the correct guess

import random
n = random.randrange(1, 10)
print("Enter a Number - ")
userinput = int(input())
while userinput != n:
    if userinput == n:
        break
    elif userinput > n:
        print("Too higher than the original one")
        userinput = int(input("Enter Number again - "))
    else:
        print("Too lower than the original one")
        userinput = int(input("Enter Number again - "))

print("Yay!! You guessed the correct number")
