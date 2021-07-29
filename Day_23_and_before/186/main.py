import turtle
import random
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

DIFFICULT = 0.1

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Score()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    ball.move()
    sleep(DIFFICULT)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if ball.xcor() <= l_paddle.xcor() + 20 and l_paddle.ycor() + 50 >= ball.ycor() >= l_paddle.ycor() - 50:
        ball.bounce_x()
        ball.increase_speed()
    if ball.xcor() >= r_paddle.xcor() - 20 and r_paddle.ycor() + 50 >= ball.ycor() >= r_paddle.ycor() - 50:
        ball.bounce_x()
        ball.increase_speed()
    if ball.xcor() <= -380:
        score.r_goal()
        ball.rest_position()
        ball.bounce_x()
    if ball.xcor() >= 380:
        score.l_goal()
        ball.rest_position()
        ball.bounce_x()

    screen.update()

screen.exitonclick()
