import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
carloop =3
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(key = "Up",fun=player.move)

score = Scoreboard()
game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    
    #creation of car for everyu 3 loop
    if carloop%3==0:
        car = CarManager()
    car.move_car()
    
    if player.ycor()>280:
        player.reset_turtle()
        car.increase_speed()
        score.level_up()
    #collison of car and turtle
    for car in car.cars:
        if player.distance(car)<20:
            score.game_over()
            game_is_on = False 
        
    carloop+=1

screen.exitonclick()