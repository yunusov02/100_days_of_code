import pandas

from turtle import Turtle
from turtle import Screen


WAY_TO_IMAGE = "D://100_days_of_code//day_25//blank_states_img.gif"
WAY_TO_CSV = "D://100_days_of_code//day_25//50_states.csv"

screen = Screen()
screen.title("State Game")
screen.addshape(WAY_TO_IMAGE)

turtle = Turtle()
turtle.shape(WAY_TO_IMAGE)

guessed_state = []

data = pandas.read_csv(WAY_TO_CSV)
all_states = data['state'].tolist()

while len(guessed_state) < 50:
    answer_date = screen.textinput(
        title="Guess the state",
        prompt="What's the another state's name"
    ).title()

    if answer_date == "Exit":
        break

    if answer_date in all_states:
        guessed_state.append(answer_date)

        t = Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_date]
        t.goto(int(state_data.x), int(state_data.y))
        
        t.write(state_data.state.item())


screen.exitonclick()
