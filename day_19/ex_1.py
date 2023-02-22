from turtle import Turtle
from turtle import Screen

turtle = Turtle()

def move_forward():
    turtle.forward(20)

def move_right():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def move_left():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def move_backward():
    turtle.backward(20)
  
def clear():
    turtle.penup()
    turtle.clear()
    turtle.home()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
