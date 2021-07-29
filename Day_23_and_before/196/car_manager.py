from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
LEVEL_SPEED_INCREASE = 2



class CarManager():
    def __init__(self):
        self.all_cars = []
        self.MOVE_INCREMENT = 10

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(random.randint(-1000, -320), random.randint(-250, 250))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() + self.MOVE_INCREMENT
            if car.xcor() < 350:
                car.goto(new_x, car.ycor())
            else:
                car.goto(random.randint(-1000, -320), random.randint(-250, 250))

    def level_up(self):
        self.MOVE_INCREMENT += LEVEL_SPEED_INCREASE

