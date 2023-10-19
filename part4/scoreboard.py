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
    #Instructor solution
    #with open("part4/data.txt", mode="r") as file:
    #  self.high_score = int(file.read())
    #My solution
    self.high_score = self.read_file_to_update_highscore()
    self.goto(0, 270)
    self.refresh()

  def refresh(self):
    self.clear()
    self.write(f"Score= {self.score} High Score: {self.high_score}", 
               align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      #Instructor solution
      #with open("part4/data.txt", mode="w") as file:
      #  file.write(f"{self.high_score})
      #My solution
      self.write_highscore_to_file()
    self.score = 0
    self.refresh()
  
  def add_score(self):
    self.score += 1
    self.refresh()
  
  #My solution
  def read_file_to_update_highscore(self):
    with open("part4/data.txt", mode="r") as file:
      high_score = file.read()
    return int(high_score)
  #My solution
  def write_highscore_to_file(self):
    with open("part4/data.txt", mode="w") as file:
      file.write(f"{self.high_score}")