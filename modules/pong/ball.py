"""Creates moving ball for Pong game"""

from turtle import Turtle

class Ball(Turtle):
    """Base class"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.setposition(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

