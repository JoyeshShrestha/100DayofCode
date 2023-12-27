from turtle import Turtle, Screen, colormode
import turtle 
from random import randint
turtle.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    timmy.color(r,g,b)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed('fastest')
a=2
n = int(360/a)
for i in range(n):
    timmy.circle(90)
    timmy.right(a)
    random_color()   

    

screen = Screen()
screen.exitonclick()