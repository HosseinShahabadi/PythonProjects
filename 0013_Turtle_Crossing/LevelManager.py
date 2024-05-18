from turtle import Turtle

FONT = ('Courier', 12, 'normal')

class LevelManager(Turtle):
    def __init__(self, screen, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.hideturtle()
        self.teleport(0, screen.window_height()/2 - 25)
        self.showLevel()


    def updateLevel(self):
        self.level += 1
        self.showLevel()


    def showLevel(self):
        '''Display the level in the upper center of the screen.'''
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def gameOver(self):
        '''Display "Game Over" in the center of the screen.'''
        self.teleport(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
