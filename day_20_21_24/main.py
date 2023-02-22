import time 

from turtle import Turtle
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# ===         Screen      ==============#  
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)   # off animated
#=======================================#

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    # Update for to see snake
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or\
        snake.head.ycor() > 290 or snake.head.ycor() < -290:
        """
        game_is_on = False
        scoreboard.game_over()
        """
        scoreboard.reset()
        snake.reset()

    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            """
            game_is_on = False
            scoreboard.game_over()
            """
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
