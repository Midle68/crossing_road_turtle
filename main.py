from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
import random
import time

screen = Screen()
screen.title("The Turtle Crossing")
screen.setup(500, 500)
screen.tracer(0)
screen.listen()

player = Player()
cars = Cars()
scoreboard = ScoreBoard()

screen.onkey(player.up, "Up")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    if random.randint(0, 5) == 1:
        cars.create_cars()
    cars.move()

    if player.ycor() > 215:
        player.reset_position()
        cars.speed += 3
        scoreboard.update_scoreboard()

    for i in cars.cars:
        if player.distance(i) < 25:
            is_on = False
            scoreboard.game_over()

screen.mainloop()
