from data import question_data
from dataclasses import dataclass

@dataclass
class Question:
    text: str
    answer: str


question_list = [Question(question['text'], question['answer']) for question in question_data]
