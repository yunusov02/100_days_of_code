from data import question_data

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    

question_bank = [Question(element["text"], element["answer"]) for element in question_data]
