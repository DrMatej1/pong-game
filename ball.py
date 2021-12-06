from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.mspeed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def bouncy(self):
        self.xmove *= -1
        self.mspeed *= 0.9

    def startup(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.mspeed = 0.1



