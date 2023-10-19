from turtle import Turtle

SCOREBOARD = 0
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color("white")
    self.score = SCOREBOARD
    self.high_score = 0
    self.goto(0, 270)
    self.refresh()

  def refresh(self):
    self.clear()
    self.write(f"Score= {self.score} High Score: {self.high_score}", 
               align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.refresh()
  
  def add_score(self):
    self.score += 1
    self.refresh()