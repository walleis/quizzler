from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain


        # Window features
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        # Labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR) # Score text
        self.score_label.grid(row=0, column=1)


        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )  # Question text
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        #Buttons
        self.true_button_image = PhotoImage(file="./images/true.png")  # True button image
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.true_pressed) # True button
        self.true_button.grid(column=0, row=2) # Button position

        self.false_button_image = PhotoImage(file="./images/false.png")  # False button image
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.false_pressed) # False button
        self.false_button.grid(column=1, row=2) # Button position

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
