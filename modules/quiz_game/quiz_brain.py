"""Brain of the quiz game"""

import html


class QuizBrain:
    """Main class of Quiz Brain"""

    def __init__(self, question_list):
        """Initialize class"""
        self.question_number = 0
        self.question_list = question_list
        self.correct_answer = ""

    def still_has_questions(self):
        """Continue if more questions in bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Ask next question and checks answer"""
        current_question = self.question_list[self.question_number]
        unescape_current_question = html.unescape(current_question.text)
        self.correct_answer = current_question.answer.lower()
        self.question_number += 1
        return f"Q.{self.question_number}: {unescape_current_question}"

    def check_answer(self, user_answer):
        """Checks answer if right or wrong"""
        return user_answer.lower() == self.correct_answer
