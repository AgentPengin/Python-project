from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_change = 10
        self.y_change = 10
        self.move_speed = 0.1

    def move(self):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.y_change *= -1

        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x,new_y)

    def refresh(self):
        self.goto(0,0)
        self.x_change *= -1
        self.y_change *= -1
        self.move_speed = 0.1


