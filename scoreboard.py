from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 215)
        self.level = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Arial", 32, "bold"))
