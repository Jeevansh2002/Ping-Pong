from turtle import *
import time
from ball_e import Ball
from paddle_e import Paddle
from scorecard_e import Scorecard

screen = Screen()
cherry = Turtle()
j=0
cherry.color("white")
screen.setup(width=700,height=500)
screen.bgcolor("black")
screen.title("Pong_Exercise")
screen.tracer(0)
ball = Ball()
scorecard = Scorecard()
r_paddle = Paddle((335,0))
l_paddle = Paddle((-340,0))

screen.listen()
screen.onkey(r_paddle.moving_up, key="Up")
screen.onkey(r_paddle.moving_down, key="Down")
screen.onkey(l_paddle.moving_up, key="w")
screen.onkey(l_paddle.moving_down, key="s")
is_game_on = True
#Divider
cherry.color("white")
cherry.left(90)
for i in range(15):
    cherry.fd(10)
    cherry.penup()
    cherry.fd(10)
    cherry.pendown()
cherry.penup()
cherry.goto(0, 0)
cherry.left(180)
for i in range(15):
    cherry.pendown()
    cherry.fd(10)
    cherry.penup()
    cherry.fd(10)
while is_game_on:
    scorecard.score()
    screen.update()
    time.sleep(0.1)
    ball.moving_ball()
    #Collision with wall
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_e()
    #Collision with r_paddle
    if ball.distance(r_paddle) < 49 and ball.xcor() > 305:
        ball.bounce_e_back()
    #Collison with l_paddle
    if ball.distance(l_paddle) < 49 and ball.xcor() < -305:
        ball.bounce_e_back()
    #Scoring
    if ball.xcor() > 340:
        scorecard.l_scoring()
        ball.goto(0,0)
        ball.bounce_e_back()
    if ball.xcor() < -350:
        scorecard.r_scoring()
        ball.goto(0,0)
        ball.bounce_e_back()
    if scorecard.r_score==1 or scorecard.l_score==1:
        cherry.pendown()
        if scorecard.l_score > scorecard.r_score:
            cherry.write(align="center", font=("courier",40,"normal"), arg=f"Winner is Left person Points:{scorecard.l_score}")
        else:
            cherry.write(align="center", font=("courier",40,"normal"), arg=f"Winner is Right person points:{scorecard.r_score}")









exitonclick()


