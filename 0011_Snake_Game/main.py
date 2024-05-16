from turtle import Screen
from SankeGame import SnakeGame
from Food import Food
from Scoreboard import Scoreboard
import time

SCREENWIDTH = 600
SCREENHEIGHT = 600


# Screen setup.
my_screen = Screen()
my_screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
my_screen.bgcolor("black")
my_screen.title('Snake Game')
my_screen.tracer(0)
my_screen.listen()

# Generating possible food positions based on screen size.
xPositions = []
yPositions = []
for i in range(int(-SCREENWIDTH/2) + 20, int(SCREENWIDTH/2), 20):
    xPositions.append(i)
for i in range(int(-SCREENHEIGHT/2) + 20, int(SCREENHEIGHT/2), 20):
    yPositions.append(i)

# Starting
snake_game = SnakeGame(my_screen)
food = Food(xPositions, yPositions, snake_game.segments)
scoreboard = Scoreboard(screenwidth=SCREENWIDTH, screenheight=SCREENHEIGHT)

game_is_on = True
food_available = True

while game_is_on:
    # Checking if Snake move is valid.
    if not snake_game.move():
        game_is_on = False
        scoreboard.gameOver()
    
    # Detect food.
    if snake_game.head.distance(food) < 10:
        snake_game.eatFood()
        food.relocate(snake_game.segments)
        scoreboard.updateScore()

    # Detect collision with wall.
    if snake_game.head.xcor() >= int(SCREENWIDTH/2) or snake_game.head.xcor() <= int(-SCREENWIDTH/2):
        game_is_on = False
        scoreboard.gameOver()
    elif snake_game.head.ycor() >= int(SCREENHEIGHT/2) or snake_game.head.ycor() <= int(-SCREENHEIGHT/2):
        game_is_on = False
        scoreboard.gameOver()


    my_screen.update()
    time.sleep(0.1)

my_screen.exitonclick()
