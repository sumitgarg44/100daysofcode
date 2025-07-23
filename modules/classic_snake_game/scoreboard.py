"""Class for Snake Game Scoreboard"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", "12", "bold")
HIGHSCORE_FILE = "static/classic_snake_game/highscore.txt"


class ScoreBoard(Turtle):
    """Scoreboard"""

    def __init__(self):
        """Initialize Scoreboard class"""
        super().__init__()
        self.hideturtle()
        self.color("cyan")
        self.penup()
        self.sety(280)
        self.high_score = self.get_highscore()
        self.score = 0
        self.update_score()

    def get_highscore(self):
        """Get Highscore"""
        with open(HIGHSCORE_FILE, mode="r", encoding="utf-8") as file:
            high_score = int(file.read())
            return high_score

    def set_highscore(self, score):
        """Set Highscore"""
        with open(HIGHSCORE_FILE, mode="w", encoding="utf-8") as file:
            file.write(str(score))

    def update_score(self):
        """Updates Score"""
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """Increment Score by 1"""
        self.score += 1
        self.update_score()

    def reset(self):
        """Reset score"""
        self.high_score = max(self.score, self.high_score)
        self.set_highscore(self.high_score)
        self.score = 0
        self.update_score()
