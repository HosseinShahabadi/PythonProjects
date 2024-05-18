from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

class Car(Turtle):
    def __init__(self, x: int, y: int, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.x = x
        self.y = y
        self.shapesize(stretch_len=2, stretch_wid=0.9)
        self.setheading(180)
        self.speed(3)
        self.teleport(x, y)
        self.penup()
        self.color(random.choice(colors))


    def move(self):
        if self.xcor() - 10 < (-self.x):
            self.teleport(self.x, self.y)
        self.forward(random.randint(1, 20))


    def relocate(self, y):
        self.teleport(self.x, y)
