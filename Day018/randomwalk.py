from turtle import Turtle, Screen, colormode
import turtle 
from random import randint
timmy = Turtle()
timmy.shape("turtle")
timmy.speed('fast')
timmy.width(6)
turtle.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    timmy.color(r,g,b)
def randomness(number):
    n = randint(10,360)
    movement= [timmy.forward(30)]
    movement[0]
    a=[0,90,180,270]
    timmy.setheading(a[number])

    
    
   




for i in range(200):
    randomness(randint(0,3))
    
    

  
    random_color()

    








screen = Screen()
screen.exitonclick()