from static.arts.rock_paper_scissor_art import draw, loose, paper, rock, scissors, win

import random

images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n")
)

if user_choice >= 3 or user_choice < 0:
    print("\nYou typed an invalid input. You loose!")
else:
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"\nComputer chooses:\n{images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print(win)
    elif computer_choice > user_choice:
        print(loose)
    elif user_choice == 2 and computer_choice == 0:
        print(loose)
    elif user_choice > computer_choice:
        print(win)
    elif user_choice == computer_choice:
        print(draw)
