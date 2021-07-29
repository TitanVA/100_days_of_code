import turtle
import random

timmy = turtle.Turtle()


def move_forward():
    return timmy.forward(10)


def turn_right():
    new_heading = timmy.heading() - 10
    return timmy.setheading(new_heading)


def turn_left():
    new_heading = timmy.heading() + 10
    return timmy.setheading(new_heading)


def move_back():
    return timmy.bk(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = turtle.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
