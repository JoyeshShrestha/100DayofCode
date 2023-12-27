import colorgram
colors = colorgram.extract('C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day018\\spot painting\\ohchampa.png', 6)
from turtle import Turtle, Screen, colormode
import turtle 
from random import randint
turtle.colormode(255)
screen = Screen()
screen.setup(width=1000, height=800)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed('normal')
rgb_list =[]
timmy.penup()
xpos=-300
ypos = -200
timmy.goto(xpos,ypos)
timmy.pendown()
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_list.append((r,g,b))
print( rgb_list)
# turtle.setpos(-10,0)

for i in range(10):
    for j in range(10):
        timmy.dot(20 , rgb_list[randint(0,5)])
        timmy.penup()
        timmy.forward(50)
    ypos+=50
    timmy.goto(xpos,ypos)
    

timmy.hideturtle()
screen.exitonclick()
