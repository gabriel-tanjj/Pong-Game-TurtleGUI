from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

# The go_up / go_down methods lives within the paddle class and once you initlize paddle1/2 as Paddle() you basically
# can call on the methods for each paddle but you have to change the key binds

#Movement for paddle 1
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
#Movement for paddle 2
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with walls
    #Change the distance to - so that when the while loop goes through its next iteration, it'll reverse the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y_axis()

    #Detect collion with paddle
    if ball.xcor() > 320 and ball.distance(paddle_1) < 50 or ball.xcor() < -320 and ball.distance(paddle_2) < 50:
        ball.ball_bounce_x_axis()

    #Detect when right paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score += 1
        scoreboard.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score += 1
        scoreboard.update_score()

screen.exitonclick()