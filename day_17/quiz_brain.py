class Brain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.number_question =  0
        self.score = 0

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("You got it")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.number_question}")
        
    
    def has_question(self):
        return self.number_question < len(self.question_list)
    
    def next_question(self):
        current_position = self.question_list[self.number_question]
        self.number_question += 1
        answer = input(f"Q {self.number_question}: {current_position.question} (True/False): ")
        self.check_answer(answer, current_position.answer)



