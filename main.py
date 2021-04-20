from turtle import Screen
from snake import Snake
import time

# Set up the screen
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Move the snake body all together; It turns off the animation

# Move the snake (i.e. the 3 objects)
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

game_is_on = True
while game_is_on:
    screen.update() # After use the 'tracer()' method, in order for it to work you need this method
    time.sleep(0.1) # Slow down the speed of the snake
    snake.move() # Move the snake--the last segment moves first

screen.exitonclick()