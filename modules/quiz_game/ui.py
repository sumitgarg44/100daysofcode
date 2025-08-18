"""Quiz Game UI"""

import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMG = "static/quiz_game/true.png"
FALSE_IMG = "static/quiz_game/false.png"


class QuizInterface:  # pylint: disable=too-many-instance-attributes
    """Base class"""

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = tkinter.Canvas(height=250, width=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.quiz_text = self.canvas.create_text(
            150,
            125,
            text="Quesiton appears here",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", "20", "italic"),
        )

        self.score_label = tkinter.Label(
            text="Score: 0",
            bg=THEME_COLOR,
            fg="white",
            highlightthickness=0,
            font=("Arial", "10", "bold"),
        )
        self.score_label.grid(row=0, column=1)

        # Buttons
        tick_img = tkinter.PhotoImage(file=TRUE_IMG)
        cross_img = tkinter.PhotoImage(file=FALSE_IMG)

        self.true_button = tkinter.Button(
            image=tick_img,
            bg=THEME_COLOR,
            borderwidth=0,
            highlightthickness=0,
            command=self.true_pressed,
        )
        self.true_button.grid(row=2, column=0)

        self.false_button = tkinter.Button(
            image=cross_img,
            bg=THEME_COLOR,
            borderwidth=0,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=2, column=1)
        # Buttons end here

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Get Next Question"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            final_text = (
                "You've completed the quiz\n"
                f"Your final score was: {self.score}/{self.quiz.question_number}"
            )
            self.canvas.itemconfig(self.quiz_text, text=final_text)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """User pressed True button"""
        is_right = self.quiz.check_answer(user_answer="true")
        self.give_feedback(is_right)

    def false_pressed(self):
        """User pressed False button"""
        is_right = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Give Feedback to user"""
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.score}")
