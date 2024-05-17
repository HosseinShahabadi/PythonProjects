from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, screen, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.screen = screen
        self.setheading(self.randomDegree())
        self.color('orange')
        self.penup()
        self.shapesize(0.8)
        self.speed(0)


    def randomDegree(self) -> int:
        degree = random.randint(1, 35)
        while degree == 9 or degree == 18 or degree == 27:
            degree = random.randint(1, 35)
        return degree * 10


    def move(self):
        self.forward(10)


    def reset(self, direction):
        self.setheading(self.randomDegree())
        self.teleport(0, 0)
    
    
    def bounce(self):
        T = self.heading()
        
        if T < 90:
            new_heading = 90 + T
        elif T < 180:
            new_heading = 180 - T
        elif T < 270:
            new_heading = 270 - T
        elif T < 360:
            new_heading = 180 + T
        
        self.setheading(new_heading)
        self.forward(30)


    def wallCollision(self, direction):
        if direction == 'down':
            self.setheading(-1*self.heading())
        else:
            self.setheading(-1*self.heading())
