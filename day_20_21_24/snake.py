from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    
    def __init__(self):
        super().__init__()
        self.segments = []
        self.body()

        self.head = self.segments[0]

    def body(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.speed(1)
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)
    
    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        
        self.segments.clear()
        self.body()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


