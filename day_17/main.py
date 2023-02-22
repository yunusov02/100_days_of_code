from question_model import question_bank
from quiz_brain import Brain

brain = Brain(question_bank)

while brain.has_question():

    brain.next_question()


print("You have completed the quiz")
print(f"Your final score was: {brain.score}/{brain.number_question}")
