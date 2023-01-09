from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
lives_tracker = Scoreboard(position=(-380, 250), lives_tracker=True)
score_tracker = Scoreboard(position=(380, 250), lives_tracker=False)


# Game Over Writing Handler


def game_over():
    game_over = Turtle()
    game_over.hideturtle()
    game_over.penup()
    game_over.pencolor('white')
    game_over.home()
    game_over.write('Game Over', move=False,
                    align='center', font=('Georgia', 50, 'normal'))


def update_file():
    with open('scores.txt', 'a') as scores:
        scores.write(f"\nPlayer Score: {score_tracker.score}")


# Setting brick properties and placing them on screen
start_x = -380
start_y = 216
x_spacing = 40
y_spacing = -30
colors = ['red', 'orange', 'yellow', 'green']
bricks = []
for color in colors:
    start_y += y_spacing
    start_x = -380
    for i in range(18):
        start_x += x_spacing
        new_coordinate = (start_x, start_y)
        brick = Brick(color, new_coordinate)
        bricks.append(brick)

screen.listen()
screen.onkeypress(fun=paddle.left, key='Left')
screen.onkeypress(fun=paddle.right, key='Right')

game_is_on = True
speed = 1
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Check win conditions by total score
    if score_tracker.score > 215:
        game_over()
        update_file()

    # Brick Removal Handler/Increase Score
    for brick in bricks:
        if ball.distance(brick) < 20:
            ball.bounce_y()
            score_tracker.increase_score(brick.fillcolor())
            ball.move_speed += 0.001
            brick.disappear()

    if ball.xcor() <= -380 or ball.xcor() >= 380:
        ball.bounce_x()
    elif ball.distance(paddle) <= 50 and ball.ycor() > -280:
        ball.bounce_y()
    elif ball.ycor() > 270:
        ball.bounce_y()
    elif ball.ycor() < -280:
        if lives_tracker.lives > 0:
            time.sleep(1)
            ball.reset_position()
            lives_tracker.deduct_life()
        else:
            game_is_on = False
            game_over()
            update_file()
            print('Game Over')


screen.exitonclick()
