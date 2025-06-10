from static.arts import guessnumber_art
from random import randint


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS
    else:
        print("\nInvalid difficulty level!")
        return 0


def check_answer(number, answer, turn):
    if number > answer:
        turn -= 1
        print("Too high")
    elif number < answer:
        turn -= 1
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}.")

    return turn


# Main code starts here
print(guessnumber_art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

EASY_TURNS = 10
HARD_TURNS = 5
computer_num = randint(1, 100)
turn = set_difficulty()
user_guess = 0

while computer_num != user_guess:
    print(f"You have {turn} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    turn = check_answer(number=user_guess, answer=computer_num, turn=turn)

    if turn == 0:
        print("You've run out of guesses!")
        break
    elif computer_num != user_guess:
        print("Guess again")
