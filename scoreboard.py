from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.display()

    def display(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score}   Highscore: {self.highscore}",
            align="center",
            font=("Courier", 18, "bold"),
        )

    def update(self):
        self.score += 1
        self.display()

    def refresh(self):
        if self.score > self.highscore:
            with open("highscore.txt", "w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.display()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(
    #         arg="GAME OVER",
    #         align="center",
    #         font=("Courier", 24, "bold"),
    #     )
