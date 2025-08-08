"""French Words Flash Cards"""

import os
import random
import tkinter

import pandas

BACKGROUND_COLOR = "#B1DDC6"
DEFAULT_WORDS_FILE = "static/french_flash_cards/french_words.csv"
UNKNOWN_WORDS_FILE = "static/french_flash_cards/words_to_learn.csv"

if os.path.exists(UNKNOWN_WORDS_FILE) and os.path.getsize(UNKNOWN_WORDS_FILE) > 1:
    DATA_FILE = UNKNOWN_WORDS_FILE
else:
    DATA_FILE = DEFAULT_WORDS_FILE

data = pandas.read_csv(DATA_FILE)
to_learn = data.to_dict(orient="records")
current_card = {}

# ----------------- Card and Flip logic ---------------------------- #


def next_card():
    """Draw next card"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    if len(to_learn) != 0:
        current_card = random.choice(to_learn)
        canvas.itemconfigure(flash_card, image=card_front)
        canvas.itemconfigure(card_title, text="French", fill="black")
        canvas.itemconfigure(card_word, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfigure(card_title, text="Bravo", fill="black")
        canvas.itemconfigure(card_word, text="Well Done!", fill="black")


def flip_card():
    """Flip card"""
    canvas.itemconfigure(flash_card, image=card_back)
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_word, text=current_card["English"], fill="white")


def is_known():
    """If words is known"""
    window.after_cancel(flip_timer)

    if len(to_learn) > 0:
        to_learn.remove(current_card)
        pandas.DataFrame(to_learn).to_csv(UNKNOWN_WORDS_FILE, index=False)

        next_card()


# ----------------- UI Setup ----------------------------- #
window = tkinter.Tk()
window.title("French words Flash Cards")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
check_image = tkinter.PhotoImage(file="static/french_flash_cards/right.png")
unknown_image = tkinter.PhotoImage(file="static/french_flash_cards/wrong.png")
card_front = tkinter.PhotoImage(file="static/french_flash_cards/card_front.png")
card_back = tkinter.PhotoImage(file="static/french_flash_cards/card_back.png")

# Buttons
check_button = tkinter.Button(
    image=check_image,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
    command=is_known,
)
check_button.grid(row=1, column=0)

unknown_button = tkinter.Button(
    image=unknown_image,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
    command=next_card,
)
unknown_button.grid(row=1, column=1)

# Canvas
canvas = tkinter.Canvas(width=800, height=526)
canvas.configure(highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
canvas.grid(row=0, column=0, columnspan=2)
flash_card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

# Card Flip timer
flip_timer = window.after(3000, flip_card)

# Get first card immediately
next_card()

window.mainloop()
