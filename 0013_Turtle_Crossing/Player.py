from turtle import Turtle

class Player(Turtle):
    def __init__(self, screen, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.screen = screen
        self.setheading(90)
        self.teleport(0, -screen.window_height()/2 + 30)
        self.penup()


    def move(self):
        self.forward(20)


    def reset(self):
        self.teleport(0, -self.screen.window_height()/2 + 30)
