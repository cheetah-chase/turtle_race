from turtle import Turtle
from random import randint

RAND_DISTANCE = randint(0, 10)


class TurtleCl(Turtle):
    """Makes Turtles and also have a move function to move the turtle you create with this class"""

    def __init__(self, position, color):
        super(TurtleCl, self).__init__()
        self.create_turtle(position, color)
        self.go_forward()

    def create_turtle(self, position, color):
        """Creates the Turtle under the turtle Class"""
        self.shape("turtle")
        self.penup()
        self.color(color)
        self.goto(position)

    def go_forward(self):
        """Move the Turtle under the turtle class"""
        new_x = self.xcor() + RAND_DISTANCE
        y = self.ycor()
        self.goto(new_x, y)
