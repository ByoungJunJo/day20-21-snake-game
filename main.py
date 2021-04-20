from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Move the snake body all together; It turns off the animation

# Move the snake (i.e. the 3 objects)
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()  # After use the 'tracer()' method, in order for it to work you need this method
    time.sleep(0.1)  # Slow down the speed of the snake
    snake.move()  # Move the snake--the last segment moves first

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()   # Update new x and y coordinates
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # If head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()