import random

numbers = range(1, 101)
guess_num = random.choice(numbers)


def easy_level():
    attempts = 10
    guessing = True

    while guessing:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == guess_num:
            print(f"You go it! The answer was {guess}")
            guessing = False

        if guess < guess_num:
            print("Too low.")
        elif guess > guess_num:
            print("Too high")
        attempts -= 1

        if attempts == 0 and guess != guess_num:
            print("You've run out of guesses, you lose. ")
            guessing = False


def hard_level():
    attempts = 5
    guessing = True

    while guessing:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == guess_num:
            print(f"You go it! The answer was {guess}")
            guessing = False

        if guess < guess_num:
            print("Too low.")
        elif guess > guess_num:
            print("Too high")
        attempts -= 1

        if attempts == 0 and guess != guess_num:
            print("You've run out of guesses, you lose. ")
            guessing = False


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

game_on = True
while game_on:

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        easy_level()
        game_on = False
    elif level == "hard":
        hard_level()
        game_on = False
    else:
        print("That's not a valid option")
