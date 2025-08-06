"""Print Phonetic words list of user supplied word"""

import pandas

from helpers.colors import color

DATA_FILE = "static/nato_conversion/nato_phonetic_alphabet.csv"


def generate_phonetic(data):
    """Generate Phonetic"""
    data = pandas.read_csv(DATA_FILE)
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    user_word = input("Enter the name or word: ").upper()

    try:
        code_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError as e:
        print(
            f"{color.RED}Invalid character {e}: Only alphabetic characters are allowed.{color.END}"
        )
        generate_phonetic(DATA_FILE)
    else:
        print(code_list)


generate_phonetic(DATA_FILE)
