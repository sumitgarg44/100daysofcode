"""Classic Snake game"""

# Standard module
import time
from turtle import Screen

# First Party
from modules.classic_snake_game.snake import Snake
from modules.classic_snake_game.food import Food
from modules.classic_snake_game.scoreboard import ScoreBoard

SCREEN = Screen()
SCREEN.setup(height=600, width=600)
SCREEN.bgcolor("black")
SCREEN.title("Classic Snake Game")
SCREEN.tracer(0)

ALL_SQUARES = []
POSITIONS = [(-20, 0), (0, 0), (20, 0)]
GAME_IS_ON = True

SNAKE = Snake()
FOOD = Food()
SCOREBOARD = ScoreBoard()

SCREEN.listen()
SCREEN.onkey(SNAKE.up, "Up")
SCREEN.onkey(SNAKE.down, "Down")
SCREEN.onkey(SNAKE.right, "Right")
SCREEN.onkey(SNAKE.left, "Left")

while GAME_IS_ON:
    time.sleep(FOOD.snake_speed)
    SCREEN.update()
    SNAKE.move()

    # Detect collison with food
    if SNAKE.head.distance(FOOD) < 15:
        FOOD.refresh()
        SNAKE.extend_body()
        SCOREBOARD.increase_score()

    # Detect collison with wall
    if (
        SNAKE.head.xcor() >= 300
        or SNAKE.head.xcor() <= -300
        or SNAKE.head.ycor() >= 300
        or SNAKE.head.ycor() <= -300
    ):
        SCOREBOARD.reset()
        FOOD.reset_speed()
        SNAKE.reset_snake()

    # Detect collison of snake head with body
    for body in SNAKE.body[1:]:
        if SNAKE.head.distance(body) < 10:
            SCOREBOARD.reset()
            FOOD.reset_speed()
            SNAKE.reset_snake()

SCREEN.exitonclick()
