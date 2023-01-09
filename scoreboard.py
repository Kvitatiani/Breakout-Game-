from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position, lives_tracker):
        super().__init__()
        self.score = 0
        self.lives = 0
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        if lives_tracker:
            self.write(f"♥️{self.lives}", False, "left",
                       ("Georgia", 30, "normal"))
        else:
            self.write(f"{self.score}", False, "right",
                       ("Georgia", 30, "normal"))

    def deduct_life(self):
        self.lives -= 1
        self.clear()
        self.write(f"♥️{self.lives}", False, "left", ("Georgia", 30, "normal"))

    def increase_score(self, color):
        if color == 'green':
            self.score += 4
        elif color == 'yellow':
            self.score += 5
        elif color == 'orange':
            self.score += 6
        else:
            self.score += 7
        self.clear()
        self.write(f"{self.score}", False, "right", ("Georgia", 30, "normal"))
