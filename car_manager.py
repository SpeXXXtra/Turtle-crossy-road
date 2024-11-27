from turtle import Turtle
import random as rm
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
speed =5


class CarManager(Turtle):
    
    cars =[]
    
    def __init__(self):
        
        super().__init__()
        self.shape("square")
        self.pu()
        self.goto(310,rm.randint(-250,280))
        self.color(COLORS[rm.randint(0,5)])
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.setheading(180)
        self.cars.append(self)
    
    def move_car(self):
        for i in self.cars:
            i.forward(speed)
    
    def increase_speed(self):
        global speed
        speed += 10
        

        