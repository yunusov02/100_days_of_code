import random

from turtle import Turtle
from turtle import Screen


# colours
colours = ["red", "blue", "green", "yellow", "purple", "orange"]

# Screen
screen = Screen()


screen.setup(width=500, height=400)
user_bit = screen.textinput(
    title="Take your bet",
    prompt="Which turtle will win the race? Enter a color:"
)

y_positions = [-70, -40, -10, 20, 50, 80]

# Turtles
all_turtles = []


for i in range(6):
    temp = Turtle(shape="turtle")
    temp.speed("fastest")
    temp.penup()
    temp.color(colours[i])
    temp.goto(x=-240, y=y_positions[i])
    all_turtles.append(temp)

is_race_on = False

if user_bit:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bit:
                print(f"You've won. The {winning_color} turtle is winner!")
            else:
                print(f"You lost")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    

screen.exitonclick()

