from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0,250)
        self.color("White")
        self.score = 0
        self.lives = 3
        with open("highscore.txt") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}     High Score = {self.high_score}     Lives = {self.lives}", align="center", font=('Arial', 20, 'normal'))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 20, 'normal'))
        with open("highscore.txt", "w") as score_update:
            score_update.write(str(self.high_score))