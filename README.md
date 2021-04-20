# day20 and 21-snake-game
## Building a snake game
### Project Description
- Build a snake game like [this](https://www.google.com/search?q=play+snake) 
- The UI isn't as fancy as the one I can find on Google but the concept is the same.
- Basically, the snake (three moving cursors or "turtles") moves around to get his snacks.

### Challenges
- Set up the screen
```
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Move the snake body all together; It turns off the animation
```

- Create a class called "Snake"
```
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a snake in fixed positions defined in Snake.py"""
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Move the snake--the last segment moves first"""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start, stop, step in order
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
```            
- Move the snake while the game is on
```
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
```
