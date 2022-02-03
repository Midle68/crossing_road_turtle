from turtle import Turtle
DEFAULT_POSITION = (0, -215)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(DEFAULT_POSITION)
        self.color("black")
        self.setheading(90)

    def up(self):
        self.forward(10)

    def reset_position(self):
        self.goto(DEFAULT_POSITION)
