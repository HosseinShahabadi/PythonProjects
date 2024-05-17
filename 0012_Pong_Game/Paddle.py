from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, screen, location, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.screen = screen
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.color('white')
        self.penup()
        self.setheading(90)
        
        if location == 'left':
            x = -screen.window_width()/2 + 15
        else:
            x = screen.window_width()/2 - 22
        
        self.teleport(x, 0)


    def automate(self, ball):
        step = 2
        if ball.xcor() < self.screen.window_width()/4 and ball.xcor() > 0:
            step = 4
        elif ball.xcor() > 0:
            step = 6
        
        if ball.ycor() + 5 > self.ycor():
            self.up(step)
        elif ball.ycor() - 5 < self.ycor():
            self.down(step)


    def up(self, step=5):
        self.forward(step)


    def down(self, step=5):
        self.backward(step)
