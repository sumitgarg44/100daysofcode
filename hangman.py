import random

from helpers.colors import color
from static.arts import gameover, hangman
from static.hangman.words import word_list

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 6

print(color.BLUE + hangman.logo + color.END)

display = []
for _ in range(word_length):
    display.append("_")

print(f"\n{color.BLUE} {' '.join(display)} {color.END}")

end_of_game = False

while not end_of_game:
    guess = input(f"\n{color.CYAN} Guess a letter: {color.END}").lower()

    if guess in display:
        print(f"\n{color.GREEN} Letter {guess} is already guessed. {color.END}")

    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index]  = letter

    if not guess in chosen_word:
        print(f"\n{color.RED} Letter {guess} not in the word. You lose a life.{color.END}")
        lives -= 1
        if lives == 0:
            print(f"\n{gameover.logo}")
            end_of_game = True
            print(f"{color.CYAN} Correct word is: {chosen_word}{color.END}")

    print(f"\n{color.BLUE} {' '.join(display)} {color.END}")

    if not "_" in display:
        print(f"\n{color.GREEN} Congratulations! You have won.{color.END}")
        end_of_game = True

    print(color.RED + hangman.stages[lives] + color.END)
