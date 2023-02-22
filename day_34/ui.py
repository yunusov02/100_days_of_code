from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import messagebox

from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
WAY_TO_IMG = "D://backend//100_days_of_code//day_34//images//"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(
            text=f"Score: {0}", 
            bg="white",
            font=("Arial", 10, "italic")
        )
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, 
            width= 280,
            text="Something", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true = PhotoImage(file=WAY_TO_IMG+"true.png")
        false = PhotoImage(file=WAY_TO_IMG+"false.png")

        self.true_button = Button(image=true, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.get_new_question()

        self.window.mainloop()

    def get_new_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            messagebox.showinfo(
                title="Score",
                message=f"You have finished\nYour current score {self.quiz.score}"
            )

    def true_answer(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_new_question)


