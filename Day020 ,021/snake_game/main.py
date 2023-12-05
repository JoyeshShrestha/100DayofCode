from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sarpa ko Game")
x_cors = 0.0
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
game_is_on = True
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision by food

    if snake.head.distance(food)< 15:
        score.add_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor()< -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        # game_is_on = False

    #Detect collision with tail

    for segment in snake.segments[1:]:
        
        
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()
    # while game_is_on:
        

    
    

    
       







screen.exitonclick()