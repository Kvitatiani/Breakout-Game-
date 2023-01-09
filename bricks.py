from turtle import Turtle

# Should create green, yellow, orange and red line of bricks.


class Brick(Turtle):

    def __init__(self, color, coordinates):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=0.8, stretch_len=1.4)
        self.penup()
        self.goto(coordinates)

    def disappear(self):
        self.hideturtle()
        self.goto(3000, -3000)
