"""Pomodoro"""

import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    """Reset Timer"""
    window.after_cancel(TIMER)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_canvas, text="00:00")
    check_marks.config(text="")
    global REPS
    REPS = 0
    start_button.configure(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(
    work_min=WORK_MIN, short_break_min=SHORT_BREAK_MIN, long_break_min=LONG_BREAK_MIN
):
    """Start timer"""
    # Disable re-execution of Start button
    start_button.config(state="disabled")

    global REPS
    work_secs = work_min * 60
    short_break_secs = short_break_min * 60
    long_break_secs = long_break_min * 60

    REPS += 1

    if REPS % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Break", fg=RED)
        window.lift()
    elif REPS % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
        window.lift()
    else:
        count_down(work_secs)
        timer_label.config(text="Work")
        window.lift()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Initiate count down"""
    mins = math.floor(count / 60)
    secs = count % 60

    if mins == 0:
        mins = "00"
    elif mins < 10:
        mins = f"0{mins}"

    if secs == 0:
        secs = "00"
    elif secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_canvas, text=f"{mins}:{secs}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 3)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.configure(bg=YELLOW, padx=100, pady=70)

timer_label = tkinter.Label(
    text="Timer", font=(FONT, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0
)
timer_label.grid(row=0, column=1)

tomato_img = tkinter.PhotoImage(file="static/pomodoro/tomato.png")
canvas = tkinter.Canvas(width=205, height=224, bg=YELLOW, bd=0, highlightthickness=0)
canvas.create_image(103, 112, image=tomato_img)
timer_canvas = canvas.create_text(
    103, 130, text="00:00", fill="white", font=(FONT, 24, "normal")
)
canvas.grid(row=1, column=1)

start_button = tkinter.Button(
    text="Start", bg=PINK, highlightthickness=0, command=start_timer
)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(
    text="Reset", bg=PINK, highlightthickness=0, command=reset
)
reset_button.grid(row=2, column=2)

check_marks = tkinter.Label(
    font=(FONT, 24, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0
)
check_marks.grid(row=3, column=1)

window.mainloop()
