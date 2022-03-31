from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#TODO 1: Create Screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-388, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
#steering left
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
#steering right
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#TODO Detect collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        # TODO Needs to bounce
        ball.bounce_y()

#TODO Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

#TODO Detect collision with black pole.
#Right Paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
#Left Paddle
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()