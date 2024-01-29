from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_distance = 10
        self.y_move_distance = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move_distance
        new_y = self.ycor() + self.y_move_distance
        self.goto(new_x, new_y)

    def ball_bounce_y_axis(self):
        """To get it to reverse direction"""
        self.y_move_distance *= -1

    def ball_bounce_x_axis(self):
        self.x_move_distance *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.ball_bounce_x_axis()