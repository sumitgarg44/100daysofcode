"""Creates scoreboard for Pong game"""

from turtle import Turtle

FONT = ("Arial", 48, "normal")

class ScoreBoard(Turtle):
    """Base class"""
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(position)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"{self.score}", font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()


        