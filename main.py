from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.moveup,key="Up")
screen.onkeypress(fun=r_paddle.movedown, key="Down")
screen.onkeypress(fun=l_paddle.moveup, key="w")
screen.onkeypress(fun=l_paddle.movedown, key="s")
flag = True

while flag:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Collision with the padddle
    if r_paddle.distance(ball) < 50 and ball.xcor() > 320 or l_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()