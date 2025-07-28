"""Print Phonetic words list of user supplied word"""

import pandas

DATA_FILE = "static/nato_conversion/nato_phonetic_alphabet.csv"
data = pandas.read_csv(DATA_FILE)
PHONETIC_DICT = {row.letter: row.code for (index, row) in data.iterrows()}
USER_WORD = input("Enter the name or word: ").upper()
CODE_LIST = [PHONETIC_DICT[letter] for letter in USER_WORD]
print(CODE_LIST)
