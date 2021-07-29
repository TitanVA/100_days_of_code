import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
Y_FINISH = 250
CARS_ON_DESK = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

game_is_on = True
while game_is_on:
    if len(car_manager.all_cars) < CARS_ON_DESK:
        car_manager.create_car()
    car_manager.move_cars()
    time.sleep(0.1)
    for car in car_manager.all_cars:
        if car.distance(player.xcor() - 2, player.ycor()) < 21:
            score.game_over()
            game_is_on = False
    if player.ycor() >= Y_FINISH:
        score.increase_score()
        player.go_start()
        CARS_ON_DESK += 10
        car_manager.level_up()
    screen.update()

screen.exitonclick()
