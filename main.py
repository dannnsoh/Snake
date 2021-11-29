from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
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

    # - Detect collision with food
    if snake.head.distance(food) <= 15:
        food.spawn()
        snake.extend()
        scoreboard.update()

    # - Detect collision with wall
    if (
        not -280 <= snake.head.xcor() <= 280
        or not -280 <= snake.head.ycor() <= 260
    ):
        scoreboard.refresh()
        snake.reset()

    # - Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) <= 10:
            scoreboard.refresh()
            snake.reset()

screen.exitonclick()
