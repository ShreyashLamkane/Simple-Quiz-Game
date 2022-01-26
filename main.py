from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

start = QuizBrain(question_bank)

while start.still_has_question():
    repeat = start.next_question()

print("You have completed your Quiz !")
print(f"Your final score is {start.score}/{start.question_no}")
