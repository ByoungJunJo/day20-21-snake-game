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

## Day 21
### Challenges
- Create food for the snake
```
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))

    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
```
- Create a scoreboard
```
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.scofrom turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", move=False, align=ALIGNMENT, font=FONT)re}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", move=False, align=ALIGNMENT, font=FONT)
```
- Detect collision with food, wall, and tail
```
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

```
## Day 23
### Challenges
- Keep highest scores by reading and writing a text file
```
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
```

### Key Takeaways
- Review class and object oriented programming in Python
- Reptition and simplicity when it comes to practice
- Google, StackOverflow, etc to figure out things when you get stuck
