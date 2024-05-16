from turtle import Turtle
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class SnakeGame:
    def __init__(self, screen) -> None:
        self.health = 3
        self.my_screen = screen
        self.segments = []

        for i in range(0, self.health):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.shapesize(1)
            new_segment.teleport(-20*i, 0)
            self.segments.append(new_segment)

        self.head = self.segments[0]


    def eatFood(self):
        '''Add another segment to the Snake'''
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.shapesize(1)
        new_segment.teleport(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)
        self.health += 1


    def move(self):
        # Relocate each piece of the Snake.
        for i in range(self.health - 1, 0, -1):
            self.segments[i].teleport(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        
        # onKey functions.
        self.my_screen.onkey(self.right, 'd')
        self.my_screen.onkey(self.left, 'a')
        self.my_screen.onkey(self.up, 'w')
        self.my_screen.onkey(self.down, 's')
        self.my_screen.onkey(self.right, 'D')
        self.my_screen.onkey(self.left, 'A')
        self.my_screen.onkey(self.up, 'W')
        self.my_screen.onkey(self.down, 'S')
        self.my_screen.onkey(self.right, 'Right')
        self.my_screen.onkey(self.left, 'Left')
        self.my_screen.onkey(self.up, 'Up')
        self.my_screen.onkey(self.down, 'Down')
        
        self.head.forward(20)

        # Detect collision with tail.
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return False
        
        return True


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
