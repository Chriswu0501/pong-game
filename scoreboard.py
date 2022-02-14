from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update()

    def l_point(self):
        self.l_score += 1
        self.update()
