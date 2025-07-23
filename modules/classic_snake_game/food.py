"""Class for Snake Food"""

import random
from turtle import Turtle

SNAKE_SPEED = 0.3


class Food(Turtle):
    """Snake Food"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.snake_speed = SNAKE_SPEED
        self.refresh()

    def refresh(self):
        """Relocate the food"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)
        self.snake_speed *= 0.9
