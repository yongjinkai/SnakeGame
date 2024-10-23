from turtle import Turtle, Screen
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(4):
            snake = Turtle(shape="square")
            snake.shapesize(stretch_wid=0.5, stretch_len=0.5)
            snake.color("white")
            snake.penup()
            snake.setpos(x=i * -20, y=0)
            snake.speed("fastest")
            self.segments.append(snake)

    def move(self):
        for number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[number - 1].xcor()
            new_y = self.segments[number - 1].ycor()
            self.segments[number].goto(new_x, new_y)
        self.segments[0].fd(10)

    def add_segment(self):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.pu()
        new_seg.setpos(self.segments[-1].pos())
        new_seg.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.segments.append(new_seg)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)
