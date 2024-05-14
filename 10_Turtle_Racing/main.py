from turtle import Turtle, Screen
import random


my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a rainbow color: ').lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtles = []
for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.setposition(x=-230, y=(- 90 + i*30))
    new_turtle.clear()
    turtles.append(new_turtle)

is_game_over = False
while not is_game_over:
    for turtle in turtles:
        if turtle.position()[0] >= 230:
            winner = turtle.color()[0]
            is_game_over = True
            break
        else:
            turtle.forward(random.randint(2, 10))

if user_bet == winner:
    msg = 'You\'ve Won;'
else:
    msg = 'You\'ve Lost;'
print(f'{msg} The {winner} turtle is the winner!')

my_screen.exitonclick()