import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))
    if guess < secret_number:
        print("too low!")
    elif guess > secret_number:
        print("too high!")
    else:
        print("correct! you guessed it!")
        break
