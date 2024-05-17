from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Wall import Wall
from Scoreboard import Scoreboard
import time

SCREENWIDTH = 800
SCREENHEIGHT = 600
TIMER = 0.05
AUTOMATION = True # Set it to 'False' for a 2-player game.

# Screen setup.
my_screen = Screen()
my_screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
my_screen.bgcolor("black")
my_screen.title('Pong')
my_screen.listen()

# Starting
Wall(my_screen, 'up')
Wall(my_screen, 'down')

paddle_left = Paddle(my_screen, 'left')
paddle_right = Paddle(my_screen, 'right')
score_board = Scoreboard(my_screen)
ball = Ball(my_screen)

timer = TIMER

while 1:
    time.sleep(timer)
    timer *= 0.9

    ball.move()
    
    if AUTOMATION:
        paddle_right.automate(ball)
        my_screen.onkeypress(paddle_left.up, 'Up')
        my_screen.onkeypress(paddle_left.down, 'Down')
    else:
        my_screen.onkeypress(paddle_right.up, 'Up')
        my_screen.onkeypress(paddle_right.down, 'Down')

    # onKeypress functions
    my_screen.onkeypress(paddle_left.up, 'w')
    my_screen.onkeypress(paddle_left.down, 's')
    my_screen.onkeypress(paddle_left.up, 'W')
    my_screen.onkeypress(paddle_left.down, 'S')

    # Detect collision with wall and bounce.
    if ball.ycor() <= (-SCREENHEIGHT/2 + 40):
        ball.wallCollision('down')
    elif ball.ycor() >= (SCREENHEIGHT/2 - 35):
        ball.wallCollision('up')

    # Detect collision with score zones.
    if ball.xcor() <= -SCREENWIDTH/2:
        timer = TIMER
        score_board.updateScore('right')
        ball.reset('right')
    elif ball.xcor() >= SCREENWIDTH/2:
        timer = TIMER
        score_board.updateScore('left')
        ball.reset('left')
    
    # Detect collision with paddles and bounce.
    if ball.xcor() <= (-SCREENWIDTH/2 + 30):
        if ball.ycor() < (paddle_left.ycor() + 20) and ball.ycor() > (paddle_left.ycor() - 20):
            ball.bounce()
    elif ball.xcor() >= (SCREENWIDTH/2 - 30):
        if ball.ycor() < (paddle_right.ycor() + 20) and ball.ycor() > (paddle_right.ycor() - 20):
            ball.bounce()


my_screen.exitonclick()
