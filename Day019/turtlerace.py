from turtle import Turtle, Screen
from random import randint
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
screen.bgpic('C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day019\\1bg.gif')
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?(Red, Blue, Green, Black, Grey) Enter a color: ").lower()
colors = ["red","blue","green","black","grey"]
x_cors = -200
y_cors = -50
all_turtle = []
for color in colors:
    turtle = Turtle("turtle")
    turtle.speed(("slow"))
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=x_cors, y=y_cors)
    y_cors+=35
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        rand_distance = randint(0,7)
        turtle.forward(rand_distance)
        
        if turtle.xcor() >= 210.0:
            winner = turtle.color()
            
            is_race_on = False

if user_bet == winner[1].lower():
    print(f"Congratulations! {user_bet} has won the race")
else:
    print(f"You lose! {winner[1]} has won the race")







screen.exitonclick()