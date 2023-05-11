#snake game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

lives = 0
score = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        scoreboard.add_score()
        snake.extend(scoreboard.score)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        screen.update()
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.reset()
            snake.reset()

    if scoreboard.lives < 1:
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()