import turtle as t
import random

color_list = [
    (242, 249, 246), (213, 154, 104), (15, 20, 73), (234, 225, 101), (51, 86, 145),
    (113, 171, 211), (168, 80, 48), (49, 29, 20), (193, 90, 123), (211, 86, 63),
    (55, 117, 51), (27, 44, 129), (111, 37, 64), (23, 45, 29), (156, 62, 88),
    (196, 135, 170), (121, 197, 161), (139, 33, 26), (64, 27, 39), (152, 211, 197),
    (98, 112, 192), (31, 89, 46), (84, 81, 32), (65, 161, 115), (150, 212, 220),
    (165, 186, 223), (226, 175, 163), (217, 176, 189), (156, 128, 89), (79, 163, 170),
    (21, 82, 98), (234, 221, 18)
]

coco = t.Turtle()
t.colormode(255)
coco.speed("fastest")

number_of_dots = 30

coco.penup()
coco.setpos(-700, -450)
coco.hideturtle()

def make_dots(num_of_dots):
    for _ in range(num_of_dots):
        coco.pendown()
        coco.dot(20, random.choice(color_list))
        coco.penup()
        coco.fd(50)
    coco.setx(-700)

for _ in range(number_of_dots):
    make_dots(number_of_dots)       
    coco.sety(coco.ycor() + 50)

screen = t.Screen()
screen.exitonclick()