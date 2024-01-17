from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())  # data is in str, convert to int

    def display_score(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score: {self.highscore}", False, align="center",
                   font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")  # pass a str to data file
        self.score = 0
        self.display_score()

    def track_score(self):
        current_score = self.score
        self.score += 1
        self.display_score()
        return current_score
