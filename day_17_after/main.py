from question_model import question_list
from quiz_brain import Quiz


quiz = Quiz(question_list)

while quiz.is_next_question():
    quiz.current_quesiton()
    print(f"{quiz.correct_answers}/{quiz.total_question}")

print("Questions complleted")
print(f"You got {quiz.correct_answers}/{quiz.total_question}")

