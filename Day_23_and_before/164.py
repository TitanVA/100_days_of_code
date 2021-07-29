import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)
radius = 75
degree = 10
pos = 0


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    color = (r, g, b)
    return color


while pos < 360:
    timmy.color(random_color())
    timmy.circle(radius)
    timmy.right(degree)
    pos += degree


screen = turtle.Screen()
screen.exitonclick()