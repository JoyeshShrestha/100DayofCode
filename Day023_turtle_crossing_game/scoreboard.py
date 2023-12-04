FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 1
        self.score_display()

    def score_display(self):

        # self.color("White")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.speed("fastest")
        self.write(f"Level : {self.score_count}",move =True,align="Center",font=FONT)


    def increaselevel(self):
        self.clear()
        self.score_count+=1    
        self.score_display()

    def game_over(self):
        self.color("Black")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.speed("fastest")
        self.write(f"GAME OVER",move =True,align="Center",font=('Courier', 25, 'normal'))    