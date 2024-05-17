from turtle import Turtle

class Wall(Turtle):
    def __init__(self, screen, location, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_len=screen.window_width()/20, stretch_wid=1)
        self.color('gray')
        self.penup()
        
        if location == 'up':
            self.teleport(0, screen.window_height()/2 - 10)
        elif location == 'down':
            self.teleport(0, -screen.window_height()/2 + 15)
        else:
            self.teleport(0, -screen.window_height()/2 + 15)
