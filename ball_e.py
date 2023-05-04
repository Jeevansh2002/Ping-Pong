from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed=0.001
        self.pendown()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10

    def moving_ball(self):
        position_x = self.xcor() + self.x
        position_y = self.ycor() + self.y
        self.goto(position_x , position_y)

    def bounce_e(self):
        self.y *= -1

    def bounce_e_back(self):
        self.x *= -1 - self.speed
        self.speed *= 1.01

