from turtle import Screen, ycor
from Player import Player
from CarsManager import CarsManager
from LevelManager import LevelManager
import time

SCREENWIDTH = 600
SCREENHEIGHT = 600
TIMER = 0.1

def isBetween(num: int, start: int, end: int):
    if start > end:
        return False
    
    if start <= num and num <= end:
        return True
    else:
        return False

# Screen setup.
my_screen = Screen()
my_screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
my_screen.bgcolor("white")
my_screen.title('Turtle Crossing')
my_screen.listen()
my_screen.tracer(0)
my_screen.window_height()

# Starting
player = Player(my_screen)
cars_manager = CarsManager(my_screen)
level_manager = LevelManager(my_screen)

timer = TIMER
game_is_on = True

while game_is_on:
    # onKey functions.
    my_screen.onkey(player.move, 'w')
    my_screen.onkey(player.move, 'Up')
    
    cars_manager.moveCars()

    # Detect collision with cars.
    if player.ycor() in cars_manager.car_positions:
        for car in cars_manager.cars:
            if player.ycor() == car.ycor() and isBetween(car.xcor(), -10, 10):
                level_manager.gameOver()
                game_is_on = False
                break
    
    # Detect collision with top wall.
    if player.ycor() >= my_screen.window_height()/2 - 30:
        level_manager.updateLevel()
        player.reset()
        timer *= 0.9
        cars_manager.increaseCars(1)
    
    time.sleep(timer)
    my_screen.update()

my_screen.exitonclick()
