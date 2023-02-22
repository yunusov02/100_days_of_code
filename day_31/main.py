import pandas
import random

from tkinter import Tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Canvas

WAY_TO_IMAGES = "D://100_days_of_code//day_31//images//"
WAY_TO_DATA = "D://100_days_of_code//day_31//data//"
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv(WAY_TO_DATA+"french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(WAY_TO_DATA+"french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ------------ NEXT WORD --------------------------------------------#

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(WAY_TO_DATA+"words_to_learn.csv", index=False)
    next_word()


def next_word():
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

# ------------------------------------------------------------------#


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=576, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=WAY_TO_IMAGES+"card_front.png")
card_back_img = PhotoImage(file=WAY_TO_IMAGES+"card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150,text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=('Arial', 60, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file=WAY_TO_IMAGES+"wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=WAY_TO_IMAGES+"right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_word()

window.mainloop()



