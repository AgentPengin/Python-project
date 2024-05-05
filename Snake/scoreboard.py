from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game over",align = "center", font = ("Courier", 15, "normal"))