"""Turtle cars crossing game"""

# Standard Library
import time
from turtle import Screen

# First party
from modules.turtle_crossing.player import Player
from modules.turtle_crossing.car_manager import CarManager
from modules.turtle_crossing.level import Level


SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.title("Turtle Crossing")
SCREEN.tracer(0)

PLAYER = Player()
LEVEL = Level()
CAR_MANAGER = CarManager()

SCREEN.listen()
SCREEN.onkey(PLAYER.go_up, "Up")

IS_GAME_ON = True

while IS_GAME_ON:
    time.sleep(0.1)
    SCREEN.update()

    CAR_MANAGER.create_car()
    CAR_MANAGER.move()

    if PLAYER.ycor() > 280:
        PLAYER.resetpos()
        CAR_MANAGER.level_up()
        LEVEL.increment_level()

    for car in CAR_MANAGER.all_cars:
        if car.distance(PLAYER) < 20:
            IS_GAME_ON = False
            LEVEL.game_over()

SCREEN.exitonclick()
