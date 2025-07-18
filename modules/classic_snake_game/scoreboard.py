"""Class for Snake Game Scoreboard"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", "12", "bold")


class ScoreBoard(Turtle):
    """Scoreboard"""

    def __init__(self):
        """Initialize Scoreboard class"""
        super().__init__()
        self.hideturtle()
        self.color("cyan")
        self.penup()
        self.sety(280)
        self.score = 0
        self.update_score()

    def update_score(self):
        """Updates Score"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment Score by 1"""
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """Stop the game"""
        self.setposition(0, 0)
        self.color("red")
        self.write("GAME IS OVER", align=ALIGNMENT, font=FONT)
