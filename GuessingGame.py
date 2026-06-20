import random

playing = True
number = str(random.randint(0,9))
print("Number guessing game. Guess the number between 0 and 9.")

while playing:
    guess = input("Enter your guess \n")
    if guess == number:
        print("You won!")
        print("The number was",number)
        break
    else:
        print("Try again!")