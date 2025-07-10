"""Quiz Game"""

from models.quiz_game.question_model import Question
from static.quiz_game.data import generate_questions
from modules.quiz_game.quiz_brain import QuizBrain

question_bank = []

USER_CHOICE = str(
    input("Do you want to select number of questions and difficulty LEVEL? (Yes/No): ")
)
if USER_CHOICE.lower() == "yes":
    num_of_questions = int(input("\nHow many questions do you want to attempt? "))
    LEVEL = str(input("Select questions difficulty LEVEL (Easy/Medium/Hard): "))

    question_data = generate_questions(
        total_questions=num_of_questions, level=LEVEL.lower()
    )
    print()  # To add newline for better readability
else:
    print("User opted for default values: 10 questions and Medium difficulty level")
    question_data = generate_questions(total_questions=10, level="medium")
    print()  # To add newline for better readability

if question_data:
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
else:
    print("Error occured in generation of question bank")

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
