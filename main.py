from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start = Turtle()

start.color("white")
start.hideturtle()
start.speed("fastest")
start.write("Press spacebar to start the game!", align="center", font=("Courier", 20, "normal"))


def start_game():
    start.clear()


screen.listen()
screen.onkeypress(key="space", fun=start_game)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

continue_game = True
while continue_game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Snake eats the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.grow()

    # Snake collides with the wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 300:
        score_board.reset_score()

    # Snake collides with its own tail
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            score_board.reset_score()

screen.exitonclick()
