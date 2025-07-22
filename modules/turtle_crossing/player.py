"""Player module of turtle crossing game"""

from turtle import Turtle

POSITION = (0, -280)
STEPS = 10


class Player(Turtle):
    """Player Base Class"""

    def __init__(self, shape="turtle"):
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.resetpos()

    def go_up(self):
        """Move player"""
        self.forward(STEPS)

    def resetpos(self):
        """Reset position"""
        self.setposition(POSITION)
