from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(align='center', font=('Ariel', 30, 'normal'), arg=f"{self.l_score}")
        self.goto(x=100, y=200)
        self.write(align='center', font=('Ariel', 30, 'normal'), arg=f"{self.r_score}")

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
