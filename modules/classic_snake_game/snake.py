"""Snake Class"""

from turtle import Turtle

start_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """Snake Class"""

    def __init__(self):
        """Initialize snake attributes"""
        self.shape = "square"
        self.color = "white"
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Creates snake"""
        for position in start_positions:
            self.new_part(position)

    def new_part(self, position):
        """Create new part of Snake body"""
        snake_body = Turtle(shape=self.shape)
        snake_body.penup()
        snake_body.color(self.color)
        snake_body.setposition(position)
        self.body.append(snake_body)

    def extend_body(self):
        """Add new part to Snake body"""
        self.new_part(self.body[-1].position())

    def move(self):
        """Move snake"""
        for snake_num in range(len(self.body) - 1, 0, -1):
            new_position = self.body[snake_num - 1].position()
            self.body[snake_num].setposition(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Snake moves up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Snake moves down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Snake moves right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Snake moves left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
