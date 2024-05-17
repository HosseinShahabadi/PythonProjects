from turtle import Turtle

FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self, screen, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color('black')
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.teleport(0, screen.window_height()/2 - 20)
        self.showScore()


    def updateScore(self, direction):
        if direction == 'right':
            self.right_score += 1
        else:
            self.left_score += 1
        
        self.showScore()


    def showScore(self):
        '''Display the score in the upper center of the screen.'''
        self.clear()
        self.write(f"Score: {self.left_score} | Score: {self.right_score}", align="center", font=FONT)


    def gameOver(self):
        '''Display "Game Over" in the center of the screen.'''
        self.teleport(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
