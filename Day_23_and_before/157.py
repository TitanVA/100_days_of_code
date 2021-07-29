from turtle import Turtle, Screen
import random

colours = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]
timmy = Turtle()


def paint_pentagon(sides, len_line):
    degree = 360 / sides
    for _ in range(sides):
        timmy.forward(len_line)
        timmy.right(degree)


for side in range(3, 10):
    timmy.color(random.choice(colours))
    paint_pentagon(side, 100)

screen = Screen()
screen.exitonclick()
