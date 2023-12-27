import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint


screen = Screen()
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
def exit():
    screen.exitonclick()      
     


def main():
    
        screen.tracer(0)
        screen.listen()
        screen.setup(width=600, height=600)
        
        scoreboard.score_display()
        player = Player()

        screen.onkey(key="Up",fun=player.move)
        game_is_on = True
        while game_is_on:
            
            
            time.sleep(0.1)

            screen.update()
            

            
            cars = CarManager(scoreboard.score_count)
            cars.move()
            all_cars = cars.return_list()
            if player.ycor() > 280:
                scoreboard.increaselevel()
                player.remove()
                cars._increase_speed()
                screen.clear()
                main()
            for car in all_cars:
                # print(cars.pos())
                if player.distance(car) < 20:

                    scoreboard.game_over()
                    game_is_on=False
                    exit()
                    # ok = False
                    
            

                
ok = True
main()     
