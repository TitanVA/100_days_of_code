from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.draw_line()
        self.hideturtle()
        self.goto(-200, 250)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.draw_line()
        self.goto(-200, 250)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def draw_line(self):
        self.goto(-300, 250)
        self.pendown()
        self.goto(300, 250)
        self.penup()
