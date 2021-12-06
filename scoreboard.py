from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore = 0
        self.rscore = 0

    def upscore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def lplus(self):
        self.lscore += 1
        self.upscore()

    def rplus(self):
        self.rscore += 1
        self.upscore()