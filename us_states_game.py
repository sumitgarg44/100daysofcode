"""US States Game"""

import time
from turtle import Turtle, Screen
import pandas

STATES_IMAGE = "static/us_states_game/blank_states_img.gif"
STATES_DATA_CSV = "static/us_states_game/50_states.csv"
GUESSED_STATES = []

SCREEN = Screen()
SCREEN.setup(width=800, height=550)
SCREEN.title("US States Game")
SCREEN.bgcolor("brown")
SCREEN.bgpic(picname=STATES_IMAGE)
TURTLE = Turtle()
TURTLE.hideturtle()
TURTLE.penup()

STATES_DATA = pandas.read_csv(STATES_DATA_CSV)

while len(GUESSED_STATES) < 5:
    time.sleep(0.5)
    ANSWER_STATE = SCREEN.textinput(
        title=f"{len(GUESSED_STATES)}/50 States correct",
        prompt="What's another state name?",
    ).title()
    IS_ANSWER_TRUE = STATES_DATA.state.eq(ANSWER_STATE)
    if not STATES_DATA[IS_ANSWER_TRUE].empty:
        STATE = STATES_DATA[IS_ANSWER_TRUE]
        STATE_X = STATE.x.item()
        STATE_Y = STATE.y.item()
        TURTLE.setposition(STATE_X, STATE_Y)
        TURTLE.write(ANSWER_STATE, align="center")
        GUESSED_STATES.append(ANSWER_STATE)

SCREEN.exitonclick()
