from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.curr_score = 0
        with open ("hiscore.txt","r") as high_score:
            self.high_score = int(high_score.read())
        self.write(f"Score: {self.curr_score}  High Score: {self.high_score}", align="center",
                   font=("Calibri", 18, "normal"))

    def update_score(self):
        self.clear()
        self.curr_score += 1
        if self.curr_score >= self.high_score:
            with open("hiscore.txt", "w") as high_score:
                high_score.write(str(self.curr_score))
        with open("hiscore.txt", "r") as high_score:
            self.write(f"Score: {self.curr_score}  High Score: {high_score.read()}", align="center",
                       font=("Calibri", 18, "normal"))

    def game_over(self):
        self.curr_score = 0
        self.clear()
        with open("hiscore.txt", "r") as high_score:
            self.write(f"Score: {self.curr_score}  High Score: {high_score.read()}", align="center",
                       font=("Calibri", 18, "normal"))
