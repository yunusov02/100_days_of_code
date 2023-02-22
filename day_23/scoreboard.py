from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-215, 250)


    def score(self):
        self.clear()
        self.own_write(f"Level: {self.level}")
    
    def game_over(self):
        self.goto(0, 0)
        self.own_write("GAME OVER")
    
    def own_write(self, string):
        self.write(
            string,
            move=False,
            align="center",
            font=FONT
        )

    def increase_score(self):
        self.level += 1


