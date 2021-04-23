from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()