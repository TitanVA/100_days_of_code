import turtle
import random


turtle.colormode(255)
timmy = turtle.Turtle()
steps = 100
directions = [0, 90, 180, 270]
# colours = ["blue", "green", "red", "cyan", "magenta", "yellow", "black"]
timmy.pensize(10)
timmy.speed(0)


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    color = (r, g, b)
    return color


for steps in range(steps):
    timmy.pencolor(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))


screen = turtle.Screen()
screen.exitonclick()