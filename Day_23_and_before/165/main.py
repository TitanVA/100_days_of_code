import turtle
import random


turtle.colormode(255)
color_list = [
    (226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171),
     (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132),
     (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96),
     (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95)]

x_pos = -225
y_pos = -225


timmy = turtle.Turtle()
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
for y_dot in range(10):
    for x_dot in range(10):
        timmy.goto(x_pos, y_pos)
        timmy.dot(30, random.choice(color_list))
        x_pos += 50
    x_pos = -225
    y_pos += 50



screen = turtle.Screen()
screen.title("Painting")
screen.screensize(100, 100)
screen.exitonclick()