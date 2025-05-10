import random
import colorgram
from turtle import Turtle, Screen

timmy = Turtle() # Initializes the Turtle class.
screen = Screen() # Initializes the Screen class.
screen.colormode(255) # Sets the color mode to rgb.

def extract_color(src_image):
    """
    Will extract 30 colors from a given image.
    After extraction, will return a list of 30 rgb tuples.
    """
    colors = colorgram.extract(src_image, 30)

    color_list = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_list.append((r,g,b))
    return color_list


def draw_10(dot_size, dot_spacing):
    """
    Will draw 10 dots in a straight line.
    User can set the dot radius and the spacing between each dot.
    """
    timmy.speed("fastest")
    for _ in range(10):
        timmy.dot(dot_size, random.choice(colors)) # Draw a dot.

        # Moves the turtle forward after every dot drawn.
        timmy.penup()
        timmy.forward(dot_spacing)
        timmy.pendown()


colors = extract_color("hirst.jpg") # Get a list of rgb tuples.
y_position = -225 # Starting Y position.
timmy.teleport(-255, y_position) # Starting turtle position.

# Draws one line of circles after another, separated by 50 pixels on the y-axis.
for _ in range(10):
    draw_10(20, 50) # Draws 10 dots.
    y_position += 50 # Updates the y-position for each iteration.
    timmy.teleport(-255, y_position) # Moves the turtle to the next position.

screen.exitonclick()