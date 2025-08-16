"""Kanye"""

import tkinter

import requests

BG_IMG = "static/kanye/background.png"
KANYE = "static/kanye/kanye.png"


def get_quote():
    """Get quote from Kanye API"""

    kanye_api = "https://api.kanye.rest"

    try:
        response = requests.get(url=kanye_api, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        quote = "Error: Exception occured in api call"
        print(f"Exception occured: {e}")
    else:
        quote = response.json()["quote"]

    if len(quote) > 55:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 20, "bold"))
    else:
        canvas.itemconfig(quote_text, text=quote)


window = tkinter.Tk()
window.title("kanye Says...")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file=BG_IMG)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file=KANYE)
kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
