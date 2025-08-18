"""Quiz Game"""

from modules.quiz_game.ques_generator import generate_questions
from modules.quiz_game.question_model import Question
from modules.quiz_game.quiz_brain import QuizBrain
from modules.quiz_game.ui import QuizInterface

question_bank = []

question_data = generate_questions()
print()  # To add newline for better readability

if question_data:
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
else:
    print("Error occured in generation of question bank")

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
