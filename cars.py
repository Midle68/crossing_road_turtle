from turtle import Turtle
import random
colors = ["yellow", "pink", "purple", "grey", "brown", "orange", "blue", "green", "red"]


class Cars:
    def __init__(self):
        self.cars = []
        self.speed = 7

    def create_cars(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(1, 2)
        car.setheading(180)
        car.goto(280, random.randint(-10 * 20, 10 * 20))
        car.color(random.choice(colors))
        self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.forward(self.speed)
