"""Level tracker for Turtle crossing game"""

from turtle import Turtle

FONT = ("Arial", 24, "normal")
POSITION = (-280, 260)


class Level(Turtle):
    """Level base class"""

    def __init__(self):
        super().__init__()
        self.level_num = 1
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)
        self.update_level()

    def update_level(self):
        """Updates level"""
        self.clear()
        self.write(f"Level: {self.level_num}", align="left", font=FONT)

    def increment_level(self):
        """Increment level"""
        self.level_num += 1
        self.update_level()

    def game_over(self):
        """Prints game over"""
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=FONT)
