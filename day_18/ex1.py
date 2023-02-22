from turtle import Turtle
from turtle import Screen
import random


turtle = Turtle()
turtle.shape("turtle")



# Challange 1
"""
This for to draw triangle square and so on

def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for i in range(3, 11):
    draw_shape(i)
"""

# Challange 2
"""
colours = [
    "CornflowerBlue", 
    "DarkOrchid", 
    "IndianRed", 
    "DeepSkyBlue", 
    "LightSeaGreen", 
    "wheat", 
    "SlateGray", 
    "SeaGreen"
]

directions = [0, 90, 180, 270]

# Change pen size
turtle.pensize(15)

# cahnge speed
turtle.speed(10)

for _ in range(50):
    turtle.color(random.choice(colours))
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

"""
screen = Screen()
screen.exitonclick()
