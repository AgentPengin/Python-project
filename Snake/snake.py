from turtle import Turtle

list_positions = [(-20,0),(0,0),(20,0)]
START_LENGTH = 3
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]
    def go(self):
        for index in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x,new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def make_snake(self):
        for index in range(START_LENGTH):
            turtle = Turtle()
            turtle.color("white")
            turtle.shape("square")
            turtle.penup()
            turtle.goto(list_positions[index])
            self.segments.append(turtle)

    def extend(self):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        turtle.goto(new_x,new_y)
        self.segments.append(turtle)

