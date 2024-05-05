from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
snake = Snake()

screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

is_game_on = True
while is_game_on:
    snake.go()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        snake.extend()
        scoreboard.show_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
        break

    for segment in snake.segments:
        if segment != snake.head and snake.head.distance(segment) < 5 and snake.head.distance(segment) > 0:
            is_game_on = False
            scoreboard.game_over()
            break

    screen.update()

screen.exitonclick()