from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


score = 0

text = Turtle(visible=False)
text.color("white")
text.penup()
text.goto(0, 365)
text.write(
    arg=f"Score: {score}",
    move=True,
    align="center",
    font=("Arial", 18, "bold"),
)

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
        food.spawn()


# TODO 6. Detect collision with wall
# TODO 7. Detect collision with tail

screen.exitonclick()
