import time
from turtle import Screen

from part5.food import Food
from part5.scoreboard import Scoreboard
from part5.snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.add_score()
    #extend snake after eat 2 times
    if scoreboard.score % 2 == 0:
      snake.extend()

  #detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #print("Wall Collision!")
    scoreboard.reset()
    snake.reset()


  #detect collision with tail
  #if head collides with any segment in the tail - trigger game_over
  for segment in snake.snake_body[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()
    


screen.exitonclick()
