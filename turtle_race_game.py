"""Turtle race to bet on"""

from turtle import Turtle, Screen
import random

SCREEN = Screen()
SCREEN.setup(width=500, height=400)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
YCORS = [-100, -60, -20, 20, 60, 100]
ALL_TURTLES = []
IS_RACE_ON = False

USER_BET = SCREEN.textinput(
    title="Make your bet",
    prompt=f"Which turtle will win the race {COLORS}? Enter a color: ",
)

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(COLORS[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=YCORS[index])
    ALL_TURTLES.append(new_turtle)

if USER_BET:
    IS_RACE_ON = True

while IS_RACE_ON:
    for turtle in ALL_TURTLES:
        if turtle.xcor() > 220:
            IS_RACE_ON = False
            WINING_COLOR = turtle.pencolor()
            if WINING_COLOR == USER_BET.lower():
                print(f"You've won! The {WINING_COLOR} turtle is the winner!")
            else:
                print(f"You've lost! The {WINING_COLOR} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

SCREEN.exitonclick()
