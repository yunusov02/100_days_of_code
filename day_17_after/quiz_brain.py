from typing import List
from question_model import Question

class Quiz:
    def __init__(self, question: List[Question]):
        self.question = question
        self.__total_question = 0
        self.__correct_answer = 0
        self.__current = 0

    def current_quesiton(self):
        answer = input(f"{self.question[self.__current].text} [True/False]: ")
        if answer == self.question[self.__current].answer:
            self.__correct_answer += 1
        self.__current += 1
        self.__total_question += 1
        

    def is_next_question(self):
        return self.__current < len(self)

    @property
    def total_question(self):
        return self.__total_question
    
    @property
    def correct_answers(self):
        return self.__correct_answer


    def __len__(self):
        return len(self.question)

