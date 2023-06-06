from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), y=new_y)

    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), y=new_y)