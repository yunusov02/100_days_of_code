from turtle import Turtle

ALIGNEMENT = "center"
FONT = ('Arial', 15, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.high_score = 0
        with open("D://100_days_of_code//day_20_21_24//score.txt", "r+") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.own_write(f"Score {self.score} High score {self.high_score}")
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("D://100_days_of_code//day_20_21_24//score.txt", "r+") as file:
                file.write(str(self.high_score))
        
        self.score = 0
        self.update_scoreboard()
    

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.own_write("GAME OVER")

    def own_write(self, string):
        self.write(
            string,
            move=False,
            align=ALIGNEMENT,
            font= FONT
        )

