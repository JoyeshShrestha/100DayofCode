from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.score = Turtle()
        self.score_count = 0
        self.score_display()

    
    def add_score(self):
        # print("nom nom")
        self.score_count+=1
        self.clear()
        self.score_display()


    def game_over(self):
        self.color("White")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.speed("fastest")
        self.write(f"GAME OVER",move =True,align="Center",font=('Courier', 25, 'normal'))

    def score_display(self):

        self.color("White")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.speed("fastest")
        self.write(f"Score : {self.score_count}",move =True,align="Center",font=('Courier', 12, 'normal'))
    
            