from turtle import Turtle
ALIGN='center'
FONT=('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score=0
        self.l_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_sboard()

    def update_sboard(self):
        self.goto(100, 250)
        self.write(f"{self.r_score}", align=ALIGN, font=FONT)
        self.goto(-100, 250)
        self.write(f"{self.l_score}", align=ALIGN, font=FONT)

    def r_scoreboard(self):
        self.r_score=self.r_score+1
        self.clear()
        self.update_sboard()


    def l_scoreboard(self):
        self.l_score = self.l_score + 1
        self.clear()
        self.update_sboard()


