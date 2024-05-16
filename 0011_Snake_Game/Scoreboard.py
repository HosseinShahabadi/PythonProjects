from turtle import Turtle

FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self, screenwidth, screenheight, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color('lightgray')
        self.score = -1
        self.hideturtle()
        self.teleport(0, screenheight/2 - 30)
        self.updateScore()


    def updateScore(self):
        '''Display the score in the upper center of the screen.'''
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)


    def gameOver(self):
        '''Display "Game Over" in the center of the screen.'''
        self.teleport(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
