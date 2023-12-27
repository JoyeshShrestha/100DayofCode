from turtle import Screen,Turtle
from first_paddle import FirstPaddle
from second_paddle import SecondPaddle
import time
from scoreboard import Scoreboard
from ball import Ball

mid_line = Turtle()
win = Turtle()


screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Ding Dong Ping Pong")
screen.tracer(0)

mid_line.hideturtle()
mid_line.speed("fastest")
mid_line.color("white")
mid_line.penup()

mid_line.goto(0,-300)
mid_line.pendown()
mid_line.setheading(90)

for i in range(20):
    mid_line.forward(20)
    mid_line.penup()
    mid_line.forward(20)
    mid_line.pendown()


screen.listen()

first_player = FirstPaddle()
second_player = SecondPaddle()
scoreboard = Scoreboard()




# first_player.first_up()
screen.onkey(key="w", fun= first_player.first_up)
screen.onkey(key="s", fun= first_player.first_down)

screen.onkey(key="Up", fun= second_player.second_up)
screen.onkey(key="Down", fun= second_player.second_down)

# screen.onkey(key="Up", fun=snake.up)
while scoreboard.p1 <5 and scoreboard.p2 <5:
    ball = Ball()

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        ball.move_forward()
            # if snake.head.distance(segment) < 10:
        for fsegment in first_player.SEGMENTS:
            if ball.ball.distance(fsegment) < 20:
        # if cords[0] >= first_player.head[0] or cords[0] >= first_player.mid[0] or cords[0] >= first_player.tail[0]:
                print("yo")
                ball.create_left_angle()
        for ssegment in second_player.SEGMENTS:
            if ball.ball.distance(ssegment) < 20:
        # if cords[0] >= first_player.head[0] or cords[0] >= first_player.mid[0] or cords[0] >= first_player.tail[0]:
                print("yos")
                ball.create_right_angle()

        if  ball.ball.ycor() > 280 or ball.ball.ycor() < -270:
            ball.create_wall_angle(ball.ball.heading())

        if ball.ball.xcor() < -400:
            ball.ball.clear()
            # print("p2")

            scoreboard.add_second_score()    
            game_is_on = False
        if ball.ball.xcor() > 390:
            ball.ball.clear()
            # print("p1")
            scoreboard.add_first_score() 
            game_is_on = False             
    # turtle.hideturtle()
mid_line.clear()
win.hideturtle()
win.penup()
win.color("white")
if scoreboard.p1 > scoreboard.p2:
         
    win.write("Player 1 Wins!",move =True,align="Center",font=('Courier', 30, 'normal'))
else:
    win.write("Player 2 Wins!",move =True,align="Center",font=('Courier', 30, 'normal'))

screen.exitonclick()