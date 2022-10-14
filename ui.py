from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
TEXT_PARAMS = ("Ariel", 10, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.q_text = self.canvas.create_text(150, 125, width=285, text="Question", font=TEXT_PARAMS)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.question_text = self.quiz_brain.next_question()
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            self.canvas.itemconfig(self.q_text, text=self.question_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You have reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))
        #self.canvas.itemconfig(bg="red")

    def give_feedback(self, answer):
        if answer == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
