from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1 = 0
        self.p2 = 0
        self.score2= Turtle()
        self.score1= Turtle()
        
        self.score_p1()
        self.score_p2()

    def score_p2(self):
        
        self.score2.hideturtle()
        self.score2.color("white")
        self.score2.penup()
        self.score2.goto(50,250)

        self.score2.write(f"{self.p2}",move =True,align="Center",font=('Courier', 25, 'normal'))

    def score_p1(self):
        self.score1.hideturtle()

        self.score1.color("white")
        self.score1.penup()
        self.score1.goto(-50,250)

        self.score1.write(f"{self.p1}",move =True,align="Center",font=('Courier', 25, 'normal')) 

    def add_second_score(self):
        self.score2.clear()
        self.p2+=1    
        self.score_p2()


    def add_first_score(self):
        self.score1.clear()
        self.p1 += 1    
        self.score_p1()    