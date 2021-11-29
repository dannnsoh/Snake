from turtle import Turtle, Screen, shape

screen = Screen()
screen.setup(width=900, height=800)

# TODO 1. Create snake body

snake = Turtle(shape="square")
snake.speed(1)
snake.penup()
snake.shapesize(0.8, 2.4)

# TODO 2. Move the snake

steps = 1000
# heading()
# tracer()
# pensize()


def m_forward():
    snake.setheading(90)
    snake.forward(steps)


def m_back():
    snake.setheading(270)
    snake.forward(steps)


def m_left():
    snake.setheading(180)
    snake.forward(steps)


def m_right():
    snake.setheading(0)
    snake.forward(steps)


screen.onkeypress(m_forward, "Up")
screen.onkeypress(m_back, "Down")
screen.onkeypress(m_left, "Left")
screen.onkeypress(m_right, "Right")
screen.listen()

# TODO 3. Create snake food

food = Turtle(shape="circle", visible=False)
food.shapesize(0.6)
food.color("#dfc05b")

# TODO 4. Detect collision with food
# TODO 5. Create scoreboard
# TODO 6. Detect collision with wall
# TODO 7. Detect collision with tail

screen.exitonclick()
