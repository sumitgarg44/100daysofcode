"""Miles to KM converter"""

import tkinter

FONT = ("Arial", 12, "normal")
BG_COLOR = "lightblue"


def miles_to_km():
    """Function to convert miles to km"""
    user_miles = float(INPUT_MILES_LABEL.get())
    user_km = round(user_miles * 1.60934, 2)
    DISTANCE_KM_LABEL.config(text=user_km)


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.configure(bg=BG_COLOR, padx=30, pady=50)

INPUT_MILES_LABEL = tkinter.Entry(width=10)
INPUT_MILES_LABEL.grid(row=1, column=2)

MILES_LABEL = tkinter.Label(text="Miles", font=FONT)
MILES_LABEL.configure(bg=BG_COLOR)
MILES_LABEL.grid(row=1, column=3)

EQUAL_TO_LABEL = tkinter.Label(text="is equal to", font=FONT)
EQUAL_TO_LABEL.configure(bg=BG_COLOR)
EQUAL_TO_LABEL.grid(row=2, column=1)

DISTANCE_KM_LABEL = tkinter.Label(text="0", font=FONT)
DISTANCE_KM_LABEL.configure(bg=BG_COLOR)
DISTANCE_KM_LABEL.grid(row=2, column=2)

KM_LABEL = tkinter.Label(text="Km", font=FONT)
KM_LABEL.configure(bg=BG_COLOR)
KM_LABEL.grid(row=2, column=3)

BUTTON = tkinter.Button(text="Calculate", command=miles_to_km)
BUTTON.configure(bg=BG_COLOR)
BUTTON.grid(row=3, column=2)

window.mainloop()
