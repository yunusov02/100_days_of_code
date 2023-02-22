import colorgram
import turtle as turtle_module
import random


# Extract 6 colors from an image.
colors = colorgram.extract('d:\\100_days_of_code\\day_18\\image.jpg', 10)


array = []
for color in colors:
    rgb = color.rgb
    r, g, b = rgb.r, rgb.g, rgb.b
    array.append((r, g, b))


turtle_module.colormode(255)

turtle = turtle_module.Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.setheading(215)
turtle.forward(300)
turtle.setheading(0)

for dot_count in range(1, 101):
    turtle.dot(20, random.choice(array))
    turtle.forward(35)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(35)
        turtle.setheading(180)
        turtle.forward(350)
        turtle.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
