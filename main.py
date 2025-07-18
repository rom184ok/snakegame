from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

try:
    while game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Check collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Check collision with wall
        if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280
        ):
            scoreboard.reset()
            snake.reset()

        # Check collision with self
        for segment in snake.segments[1:]:  # skip head
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

except Exception as e:
    print(f"Error in game loop: {e}")

screen.exitonclick()
