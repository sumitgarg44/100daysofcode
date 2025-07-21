# Standard modules
from turtle import Screen
import time

# First party
from modules.pong.ball import Ball
from modules.pong.paddle import Paddle
from modules.pong.scoreboard import ScoreBoard

SCREEN = Screen()
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Pong")
SCREEN.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
BALL = Ball()
r_score = ScoreBoard(position=(100, 220))
l_score = ScoreBoard(position=(-100, 220))

SCREEN.listen()
SCREEN.onkey(r_paddle.move_up, "Up")
SCREEN.onkey(r_paddle.move_down, "Down")
SCREEN.onkey(l_paddle.move_up, "w")
SCREEN.onkey(l_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(BALL.move_speed)
    SCREEN.update()
    BALL.move()

    if BALL.ycor() > 280 or BALL.ycor() < -280:
        BALL.bounce_y()
    
    if BALL.distance(r_paddle) < 50 and BALL.xcor() > 330 or BALL.distance(l_paddle) < 50 and BALL.xcor() < -330:
        BALL.bounce_x()
    
    if BALL.xcor() > 380:
        BALL.reset_position()
        l_score.increment_score()

    if BALL.xcor() < -380:
        BALL.reset_position()
        r_score.increment_score()
    
SCREEN.exitonclick()