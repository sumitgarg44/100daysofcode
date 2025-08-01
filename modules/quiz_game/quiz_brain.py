"""Brain of the quiz game"""


class QuizBrain:
    """Main class of Quiz Brain"""

    def __init__(self, question_list):
        """Initialize class"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Continue if more questions in bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Ask next question and checks answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks answer if right or wrong"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
