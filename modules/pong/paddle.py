"""Creates paddle for Pong game"""

from turtle import Turtle

class Paddle(Turtle):
    """Base class"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)
        self.speed("fastest")

    def move_up(self):
        """Move paddle up"""
        if self.ycor() < 240:
           new_ycor = self.ycor() + 20
           self.sety(new_ycor)

    def move_down(self):
        """Move paddle down"""
        if self.ycor() > -240:
           new_ycor = self.ycor() - 20
           self.sety(new_ycor)


