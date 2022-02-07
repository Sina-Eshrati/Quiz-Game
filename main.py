from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)
while not quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz\nYour final score is {quiz.current_score}/{quiz.question_number}")
