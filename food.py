from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle", visible=False)
        self.penup()
        self.speed(10)
        self.color("#cfcfcf")
        self.shapesize(0.5, 0.5)

    def spawn(self):
        self.hideturtle()
        self.goto(randint(-380, 380), randint(-380, 360))
        self.showturtle()
