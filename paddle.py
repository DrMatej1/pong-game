from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.paddlestart()
        self.setposition(x)

    def paddlestart(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)