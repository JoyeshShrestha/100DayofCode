from turtle import Turtle
from random import randint
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []

class CarManager(Player):
    def __init__(self,level) :
        # super().__init__()
        self.y = randint(-250,250)
        self.position = (320,self.y)
        self.tufan = STARTING_MOVE_DISTANCE

        # self.all_cars =[]
        self.movement = STARTING_MOVE_DISTANCE
        self.create_cars(level)
        
    def create_cars(self,level):
            self.car= Turtle()
            self.car.penup()
            self.car.goto(self.position)
            self.car.shape("square")
            self.car.color(COLORS[randint(0,len(COLORS)-1)])
            self.car.shapesize(stretch_len=2)
            self.raftaar(level)
            
            self.car.goto(self.position)
        
            all_cars.append(self.car)
            # self.move(self.car)

    def move(self):

        for car in all_cars[0::3]: 
           
                    x = car.xcor()
                    y=car.ycor()
                    x-=self.tufan
                    gohere = (x,y)
                    car.goto(gohere)
                    

       
    def raftaar(self,level):
          if level == 1:
                pass
          else:
            for i in range(level-1):
                self.tufan += MOVE_INCREMENT 

          
          

    def _increase_speed(self):
          self.car.hideturtle()
          all_cars.clear()  

          

    def return_list(self):
        return all_cars

