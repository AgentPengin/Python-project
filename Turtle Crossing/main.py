import car_manager
from player import Player
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
player = Player()
scoreboard = Scoreboard()
carManager = CarManager()
screen.setup(width = 600,height = 600)

screen.tracer(0)
screen.listen()

screen.onkey(player.move_up,"Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >= 280:
        player.refresh()
        scoreboard.refresh()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT

    carManager.all_car_move()
    carManager.create_car()
    for car in carManager.list:
        if player.distance(car) < 23:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()