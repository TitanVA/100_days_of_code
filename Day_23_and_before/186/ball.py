import turtle
SPEED_X = 10
SPEED_Y = 10


class Ball(turtle.Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.x = 0
        self.y = 0
        self.speed_x = SPEED_X
        self.speed_y = SPEED_Y
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)

    def move(self):
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

    def rest_position(self):
        self.goto(0, 0)
        self.speed_x = 10
        self.speed_y = 10

    def increase_speed(self):
        self.speed_x *= 1.1
        self.speed_y *= 1.1
