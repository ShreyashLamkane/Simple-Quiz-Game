class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        answer = input(f"Q.{self.question_no + 1}: {self.question_list[self.question_no].text} True/False ").title()
        self.check_answer(answer)
        self.question_no += 1

    def check_answer(self, answer):
        if self.question_list[self.question_no].answer == answer:
            self.score += 1
            print("You are correct!")
            print(f"Your Score is {self.score}/{self.question_no + 1}")
            print("\n")
        else:
            print(f"Your Score is {self.score}/{self.question_no + 1}")
            print("You are incorrect!")
            print("\n")
