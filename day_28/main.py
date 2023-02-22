import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_PNG = "D://100_days_of_code//day_28//tomato.png"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='TIMER', fg=GREEN)
    check_marks.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):    
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = "✔" * (reps//2)
        check_marks.config(text=f'{mark}')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomidoro')
window.config(padx=50, pady=50, bg=YELLOW)

timer_label = Label(
    text="TIMER", 
    fg=GREEN, 
    highlightthickness=0,
    bg=YELLOW,
    font=(FONT_NAME, 30, 'bold')
)
timer_label.grid(column=1, row=0)

canvas = Canvas(
    width=200, 
    height=224, 
    bg=YELLOW, 
    highlightthickness=0
)
tomato_img = PhotoImage(file=TOMATO_PNG)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, 
    text="00:00", 
    font=(FONT_NAME, 25, 'bold'),
    fill='white'
)
canvas.grid(column=1, row=1)
    
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'bold'))
check_marks.grid(column=1, row=3)


window.mainloop()

