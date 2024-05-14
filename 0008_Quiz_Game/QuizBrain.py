import random


class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.question_bank = question_bank
        self.index = 0
        self.score = 0


    def next_question(self):
        '''Ask the user the next question and evaluate their answer.'''
        question = self.question_bank[self.index]
        text = question.text
        self.index += 1
        user_answer = input(f'Q.{self.index}: {text} (True/False)?: ').lower()
        if not self.check_answer(user_answer, question.answer):
            print("That's wrong.")
        else:
            self.score += 1
            print('You got it right!')
        print(f"Your current score is {self.score}/{self.index}\n")


    def check_answer(self, user_answer, question_answer):
        return user_answer == question_answer


    def still_has_questions(self):
        '''Return True if there are unanswered questions, False otherwise.'''
        if self.index >= len(self.question_bank):
            return False
        else:
            return True
