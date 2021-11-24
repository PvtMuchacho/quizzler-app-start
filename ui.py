from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #------ Create Window ------#
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # ------ Create white canvas ------#
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # ------ Create False Button ------#
        self.cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.cross_image, highlightthickness=0, command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1, pady=5)
        # ------ Create True Button ------#
        self.check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.check_image, highlightthickness=0, command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)
        # ------ Create Label for Score ------#
        self.score_label = Label(text=f"Score: {self.quiz.score}")
        self.score_label.config(bg=THEME_COLOR,fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def update_score(self):
        updated_score = f"{self.quiz.score}"
        self.score_label.config(text=f"Score: {updated_score}")

    def true_button_clicked(self):
        user_answer="True"
        check_answer = self.quiz.check_answer(user_answer)
        if check_answer == True:
            self.canvas.config(bg="red")
        time.sleep(5)
        self.canvas.config(bg="white")
        self.get_next_question()
        self.update_score()

    def false_button_clicked(self):
        user_answer="False"
        check_answer = self.quiz.check_answer(user_answer)
        self.get_next_question()
        self.update_score()

    def



