import random
from helpers.clear_screen import clear_screen
from helpers.colors import color
from static.higher_lower.data import data
from static.arts.higher_lower_art import logo, versus

# variables
is_wrong = 0
score = 0
celebrity_list = data
celebrityA = []
celebrityB = []

# Print logo
def print_logo():
    clear_screen()
    print(logo)

# Format Data
def format_data(person_data):
    person_name = person_data['name']
    person_descripton = person_data['description']
    person_country = person_data['country']
    return f"{person_name}, a {person_descripton}, from {person_country}."

# Find guess is correct
def is_guess_correct(person1, person2, guess):
    if guess == 'a' and person1['follower_count'] > person2['follower_count']:
        return True
    elif guess == 'b' and person1['follower_count'] < person2['follower_count']:
        return True
    else:
        return False

# Loop Print logo and statements, second iteration should print score or exit if ans is incorrect
while not is_wrong:
    print_logo()
    
    if score != 0:
        print(f"{color.PURPLE}You're right! Current score: {score}{color.END}\n")

    if not celebrityA:
        celebrityA = random.choice(celebrity_list)
    else:
        celebrityA = celebrityB
    
    celebrityB = random.choice(celebrity_list)
    while celebrityA == celebrityB:
        celebrityB = random.choice(celebrity_list)

    print(f"Compare A: {format_data(celebrityA)}")
    print(versus)
    print(f"Against B: {format_data(celebrityB)}")
    guess = input(f"\n{color.BLUE}Who has more followers? Type 'A' or 'B': {color.END}").lower()

    if is_guess_correct(person1=celebrityA, person2=celebrityB, guess=guess):
        score += 1
    else:
        print_logo()
        print(f"{color.BOLD}{color.RED}Sorry, that's wrong. Final score: {score}{color.END}{color.END}")
        is_wrong = 1