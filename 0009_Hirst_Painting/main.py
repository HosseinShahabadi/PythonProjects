from turtle import Turtle, Screen
import turtle, random, colorgram


def random_color():
    '''Returns a random color.'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def extract_colors_from_image(image: str, no_colors: int):
    '''Extract number of colors from sample image and return a list of tuples.'''
    sample = colorgram.extract(image, no_colors)
    colors = []

    for color in sample:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        tuple = (r, g, b)
        colors.append(tuple)
    
    return colors


def random_walk(timy: Turtle, no_walk: int, pensize: int=5, randomcolor: bool=True):
    '''Do a Random Walk.'''
    my_turtle.pensize(pensize)
    moves = [0, 90, 180, 270]
    for _ in range(no_walk):
        if randomcolor:
            timy.color(random_color())
        timy.setheading(random.choice(moves))
        timy.forward(20)


def draw_spirograph(timy: Turtle, gap: int=2, pensize: int=2):
    '''Draw a Spirograph.'''
    my_turtle.pensize(pensize)
    for _ in range(int(360/gap)):
        timy.color(random_color())
        timy.circle(100)
        timy.left(gap)


def draw_hist_painting(timy: Turtle, colors):
    '''Draw a Hirst Spot Paintings.'''
    timy.hideturtle()
    for i in range(0, 451, 50):
        for j in range(0, 451, 50):
            timy.teleport(-225 + j, -225 + i)
            timy.dot(18, random.choice(colors))


turtle.colormode(255)

my_turtle = Turtle()
my_turtle.shape('classic')
my_turtle.shapesize(1)
my_turtle.speed(0)


# random_walk(my_turtle, 100, 5)
# draw_spirograph(my_turtle, gap=3)
draw_hist_painting(my_turtle, extract_colors_from_image('sample.jpg', 25))


my_screen = Screen()
my_screen.exitonclick()