from question_model import Question
from quiz_brain import QuizBrain
from data import question_data



print(len(question_data))

question_bank = []
for question in question_data:
    question_text =  question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"End of the quiz. Your final score is {quiz.score}/{quiz.question_number}")



