from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 365)
        self.display()

    def display(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}",
            align="center",
            font=("Courier", 18, "bold"),
        )

    def update(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            align="center",
            font=("Courier", 24, "bold"),
        )
