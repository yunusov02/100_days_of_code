from turtle import Turtle
from turtle import Screen
from random import choice

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

turle = Turtle()
turle.shape("classic")
turle.speed("fastest")

turns = 10
for _ in range(36):
    turle.circle(75)
    turle.color(choice(colours))
    turle.home()
    turle.right(turns)
    turns += 10


screen = Screen()
screen.exitonclick()
