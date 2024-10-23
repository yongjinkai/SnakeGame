from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(n=0)
screen.listen()

slyther = Snake()
food = Food()
score = Scoreboard()

screen.onkey(slyther.up, "Up")
screen.onkey(slyther.down, "Down")
screen.onkey(slyther.left, "Left")
screen.onkey(slyther.right, "Right")

game_is_on = True
while game_is_on:
    if slyther.segments[0].distance(food) < 5:
        food.new_food()
        score.update_score()
        slyther.add_segment()
    slyther.move()
    screen.update()
    time.sleep(0.05)

    if slyther.segments[0].xcor() > 290 or slyther.segments[0].xcor() < -290 or slyther.segments[0].ycor() > 290 or \
            slyther.segments[0].ycor() < -290:
        slyther.reset()
        score.game_over()

    for i in slyther.segments[1:]:
        if slyther.segments[0].distance(i) < 5:
            score.game_over()

screen.exitonclick()
