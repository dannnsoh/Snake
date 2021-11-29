from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
food.spawn()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # todo: detect collision with food
    if snake.head.distance(food.position()) <= 15:
        scoreboard.update()
        food.spawn()

    # todo: Detect collision with wall
    if (
        not -380 <= snake.head.xcor() <= 380
        or not -380 <= snake.head.ycor() <= 360
    ):
        scoreboard.game_over()
        gameOn = False

    # todo: Detect collision with tail
    for n in range(1, len(snake.segments) - 1):
        seg = snake.segments[n]
        if snake.head.distance(seg.position()) <= 15:
            scoreboard.game_over()
            gameOn = False

screen.exitonclick()
