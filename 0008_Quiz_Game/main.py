from Question import Question
from data import question_data
from QuizBrain import QuizBrain


question_bank = []
for i in range(len(question_data)):
    question = Question(question_data[i]['text'], question_data[i]['answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f'Your final score is {quiz_brain.score}/{quiz_brain.index}')