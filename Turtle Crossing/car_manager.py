from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.list = []

    def rand_car(self):
        tmp = Turtle()
        new_y = random.randint(-280,280)
        tmp.penup()
        tmp.shape("square")
        tmp.color(COLORS[random.randint(0,len(COLORS) - 1)])
        tmp.turtlesize(stretch_len = 1.8,stretch_wid = 1)
        tmp.goto(350,new_y)
        self.list.append(tmp)

    def all_car_move(self):
        for car in self.list:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())
            if (car.xcor() < -400):
                self.list.remove(car)


    def create_car(self):
        percent = random.randint(0,5)
        if percent == 1:
            self.rand_car()





