from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.score = Label(text=f"Score: 0",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        
        self.question_text = self.canvas.create_text(150, 120, text=f"SOME", width=280, font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)
        
        
        right_img = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day034-QUIZLER\\images\\true.png")
        self.right = Button(image=right_img,highlightthickness=0,padx=20, pady=20,command=self.correct_pressed)
        wrong_img = PhotoImage(file="C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day034-QUIZLER\\images\\false.png")
        self.wrong = Button(image=wrong_img,highlightthickness=0,padx=20, pady=20,command=self.false_pressed)
        self.wrong.grid(row=2, column=1)
        self.right.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            # print("hellooo",q_text)
            self.canvas.itemconfig(self.question_text,text=q_text)

        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")


    def correct_pressed(self):
        ok,ans = self.quiz.check_answer("True")
        # self.get_next_question()
        self.change_score(ok,ans)



    def false_pressed(self):
        ok,ans = self.quiz.check_answer("False")
        # self.get_next_question()
        print(ok)
        self.change_score(ok,ans)
        

    def change_score(self,score:int,ans:bool):
        self.score.config(text=f"Score: {score}")
        if ans:

            self.canvas.config(bg="green")



        else:
            self.canvas.config(bg="red")
            


        self.window.after(1000,self.get_next_question)

        # self.canvas.config(bg="white")



