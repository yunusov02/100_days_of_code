import time

from turtle import Turtle
from turtle import Screen


from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(player.move, 'Up')
screen.onkey(player.back, "Down")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    scoreboard.score()

    car_manager.create_cars()
    car_manager.move_cars()


    if not player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_score()

    
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
