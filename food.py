from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.new_food()
    def new_food(self):
        x = random.randrange(-280,280,20)
        y = random.randrange(-280,280,20)
        self.goto(x,y)
