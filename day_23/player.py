from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move()
    
    def move(self):            
        self.forward(10)
    
    def is_at_finish_line(self):
        if self.ycor() < FINISH_LINE_Y:
            return True
        False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
