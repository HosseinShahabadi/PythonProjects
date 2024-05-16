from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, xPositions, yPositions, segments, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.xPositions = xPositions
        self.yPositions = yPositions
        self.relocate(segments)
        self.color("red")
        self.shapesize(0.5)

    def relocate(self, segments):
        '''Relocate food'''
        x = random.choice(self.xPositions)
        y = random.choice(self.yPositions)
        while not self.checkLocation(x, y, segments):
            x = random.choice(self.xPositions)
            y = random.choice(self.yPositions)

        self.teleport(random.choice(self.xPositions), random.choice(self.yPositions))


    def checkLocation(self, x, y, segments):
        '''Return False if there is a snake segment at the specified location.'''
        for seg in segments:
            if seg.distance((x, y)) < 10:
                return False
        
        return True