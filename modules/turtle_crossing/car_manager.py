"""Car Manager for Turtle crossing game"""

from turtle import Turtle
import random

COLORS = ["red", "yellow", "blue", "green", "blue", "cyan", "purple"]
MOVE_DISTANCE = 5


class CarManager:
    """Car Manager Base class"""

    def __init__(self):
        self.all_cars = []
        self.cars_speed = MOVE_DISTANCE

    def create_car(self):
        """Create car"""
        should_generate_car = random.randint(1, 4)

        if should_generate_car == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            new_car.setposition(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        """Move cars"""
        for car in self.all_cars:
            if car.xcor() > -340:
                car.backward(self.cars_speed)

    def level_up(self):
        """Increase cars speed"""
        self.cars_speed += MOVE_DISTANCE
