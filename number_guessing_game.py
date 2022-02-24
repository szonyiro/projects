import random
from replit import clear


def welcome():
    print(f"Welcome to the Number Guessing Game!"
          f"\nI'm thinking of a number between 1 and 100")


welcome()
easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game():
    keep_guessing = True
    random_number = int(random.randint(1, 100))
    attempts = int()
    if easy_or_hard == "easy":
        attempts += 10
    else:
        attempts += 5
    # print(f"Hint for testing: {random_number}")
    clear()
    while keep_guessing:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            keep_guessing = False
            clear()
            print(f"Well done, you got it. The number was {random_number}")
        elif guess < random_number:
            attempts -= 1
            print("Too low.\nGuess again!")
        elif guess > random_number:
            attempts -= 1
            print("Too high.\nGuess again!")
        if attempts == 0:
            keep_guessing = False
            clear()
            print(f"Game over!\nYou ran out of guesses.\nThe number was: {random_number}")


game()
