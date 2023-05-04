from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super(). __init__()
        self.l_score = 0
        self.r_score = 0

    def score(self):
        self.penup()
        self.clear()
        self.goto(-50,210)
        self.color("white")
        self.write(align="center",font=("courier", 30, "normal"), arg=f"L:{self.l_score}")
        self.goto(50,210)
        self.write(align="center",font=("courier", 30, "normal"), arg=f"R:{self.r_score}")
        self.hideturtle()

    def l_scoring(self):
        self.l_score += 1

    def r_scoring(self):
        self.r_score += 1






