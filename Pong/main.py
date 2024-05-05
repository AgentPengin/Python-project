from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.down, "Down")
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_change *= -1
        ball.move_speed *= 0.9

    if ball.xcor() > 400:
        ball.refresh()
        scoreboard.r_point()

    if ball.xcor() < -400:
        ball.refresh()
        scoreboard.l_point()

screen.exitonclick()
