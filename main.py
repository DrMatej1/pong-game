from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

pad1 = Paddle((350, 0))
pad2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(pad1.up, "Up")
screen.onkey(pad1.down, "Down")
screen.onkey(pad2.up, "w")
screen.onkey(pad2.down, "s")


game_on = True

while game_on:
    score.upscore()
    time.sleep(ball.mspeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(pad1) < 50 and ball.xcor() > 320 or ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.bouncy()

    if ball.xcor() > 380:
        ball.startup()
        score.lplus()

    if ball.xcor() < -380:
        ball.startup()
        score.rplus()


screen.exitonclick()


