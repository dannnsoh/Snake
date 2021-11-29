from turtle import Turtle, Screen
from random import randint
import time
from snake import Snake

screen = Screen()
screen.setup(width=900, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

# TODO 2. Move the snake

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.03)
    snake.move()


# TODO 3. Create snake food

food = Turtle(shape="circle", visible=False)
food.penup()
food.speed(10)
food.color("white")


def spawn_food():
    food.hideturtle()
    food.goto(randint(-430, 430), randint(-380, 365))
    food.showturtle()


spawn_food()


# TODO 4. Detect collision with food

# snake_x, snake_y = snake.position()
food_x, food_y = food.position()

# while (
#     food_x - 10 <= snake_x <= food_x + 10
#     or food_y - 10 <= snake_y <= food_y + 10
# ):
#     print("EAT")
#     spawn_food()

# TODO 5. Create scoreboard

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

# TODO 6. Detect collision with wall
# TODO 7. Detect collision with tail

screen.listen()
screen.exitonclick()
