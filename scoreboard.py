from turtle import Turtle
FONT = ("Courier", 18,"bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level =0
        self.pu()
        self.hideturtle()
        self.goto(-280,270)
        self.write(f"level:{self.level}",align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT)
        
    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"level:{self.level}", align="left", font=FONT)