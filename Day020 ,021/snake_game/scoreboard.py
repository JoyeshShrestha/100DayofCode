from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.score = Turtle()
        try:
            with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day020 ,021\\snake_game\\highscore.txt") as file:

            
                self.highscore = int(file.read())
        except:
                self.highscore = 0
        self.score_count = 0
        self.score_display()

    
    def add_score(self):
        # print("nom nom")
        self.score_count+=1
        self.clear()
        self.score_display()
    
    
    def save_highlight(self):
        with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day020 ,021\\snake_game\\highscore.txt","w") as file:
            file.write(str(self.highscore))




    def reset(self):
        if self.score_count > self.highscore:
            self.highscore = self.score_count
        self.score_count = 0
        self.clear()  
        self.score_display() 
        self.save_highlight() 
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
        self.write(f"Score : {self.score_count} HighScore: {self.highscore}",move =True,align="Center",font=('Courier', 12, 'normal'))
    
            