import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto((0, 200))
        self.display()

    def l_goal(self):
        self.l_score += 1
        self.clear()
        self.display()

    def r_goal(self):
        self.r_score += 1
        self.clear()
        self.display()

    def display(self):
        self.write(f"{self.l_score}:{self.r_score}", align="center", font=("Courier", 80, "normal"))