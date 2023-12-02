from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self ):
        super().__init__()
        self.ball = Turtle()
        self.generate_ball()
        self.angle_ball()

    def generate_ball(self):
        self.ball.shape("circle") 
        self.ball.speed("slow")
        self.ball.penup()
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=0.5,stretch_len=0.5)   

    def angle_ball(self):   
        angle = randint(1,360)
        self.ball.setheading(angle)
        

    def move_forward(self):
        self.ball.forward(20)    
    
    def create_left_angle(self):
        angle = 180 -randint(90,270)
        print(angle)
        if angle <= 95 and angle >= 90:
           self.create_left_angle()
        if angle <= 180 and angle >= 175:
           self.create_left_angle()    
        self.ball.setheading(angle)

    def create_right_angle(self):
        angle = randint(90,270)
        print(angle)
        if angle <= 95 and angle >= 90:
           self.create_left_angle()
        if angle <= 180 and angle >= 175:
           self.create_left_angle()    
        self.ball.setheading(angle)    


    def create_wall_angle(self,current_angle):
        # new_angle = 190
        print(current_angle)
        new_angle = 360 -(current_angle)
        self.ball.setheading(new_angle)
