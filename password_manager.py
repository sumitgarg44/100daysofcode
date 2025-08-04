"""Password Manager"""

import os
import sys
import tkinter
from random import choice, randint, shuffle
from tkinter import messagebox

import pyperclip

LOGO = "static/arts/password_manager/logo.png"
DATA_FILE = "/home/sumi6119/password_data.txt"


# ---------------------------- Get Absoluete Path ------------------------------- #
def resource_path(relative_path):
    """Converts relative to absoluete path"""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate random password"""
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    pass_letters = [choice(letters) for _ in range(0, randint(8, 11))]
    pass_symbols = [choice(symbols) for _ in range(0, randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(0, randint(2, 4))]

    pass_list = pass_letters + pass_symbols + pass_numbers

    shuffle(pass_list)

    password = "".join(pass_list)

    # Ensure password entry is empty
    password_entry.delete(0, tkinter.END)

    # Enter random generated password
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save Password"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(
            title=website, message="Please make sure you haven't left any field empty!"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \n\nEmail: {email}\n"
                f"Password: {password}\n\nIs it ok to save?",
        )

        if is_ok:
            with open(DATA_FILE, mode="a", encoding="utf-8") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("My Password Manager")
window.configure(padx=50, pady=50, bg="white")

pass_logo = tkinter.PhotoImage(file=resource_path(LOGO))
canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(120, 100, image=pass_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:", bg="white", highlightthickness=0)
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:", bg="white", highlightthickness=0)
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:", bg="white", highlightthickness=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tkinter.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sumitgarg44@gmail.com")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass_button = tkinter.Button(
    text="Generate Password",
    bg="white",
    highlightthickness=0,
    command=generate_password,
)
generate_pass_button.grid(row=3, column=2)
add_button = tkinter.Button(
    text="Add", width=40, bg="white", highlightthickness=0, command=save
)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
