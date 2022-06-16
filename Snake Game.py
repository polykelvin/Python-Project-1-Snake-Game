# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
score_announcement = "Score : {} High Score : {} "

widths = turtle.numinput("Width", "What is the width of the map", default=600, minval=0)
heights = turtle.numinput("Height", "What is the height of the map", default=600, minval=0)

# Creating a window screen
SnakeGame = turtle.Screen()
SnakeGame.title("Snake Game")
SnakeGame.bgcolor("blue")

# the width and height can be put as user's choice
SnakeGame.setup(width=widths, height=heights)
SnakeGame.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center", font=("candara", 24, "bold"))


# assigning key directions
def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"


def goLeft():
    if head.direction != "right":
        head.direction = "left"


def goRight():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


def exitGame():
    turtle.bye()
    print("Game exit, good bye")


SnakeGame.listen()
SnakeGame.onkeypress(goUp, "w")
SnakeGame.onkeypress(goUp, "Up")
SnakeGame.onkeypress(goDown, "s")
SnakeGame.onkeypress(goDown, "Down")
SnakeGame.onkeypress(goLeft, "a")
SnakeGame.onkeypress(goLeft, "Left")
SnakeGame.onkeypress(goRight, "d")
SnakeGame.onkeypress(goRight, "Right")
SnakeGame.onkeypress(exitGame, "Escape")

segments = []

# Main Gameplay
while True:
    SnakeGame.update()
    if head.xcor() > (widths / 2 - 10) or head.xcor() < (-abs(widths) / 2 - 10) or head.ycor() > (
            heights / 2 - 10) or head.ycor() < (-abs(heights) / 2 - 10):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(score_announcement.format(score, high_score), align="center", font=("candara", 24, "bold"))

    if head.distance(food) < 20:
        x = random.randint(int(((-abs(widths) / 2) + 30)), int(((widths / 2) - 30)))
        y = random.randint(int(((-abs(heights) / 2) + 30)), int(((heights / 2) - 30)))
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10

        # update the highest score
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(score_announcement.format(score, high_score), align="center", font=("candara", 24, "bold"))

    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])

            for segment in segments:
                segment.goto(1000, 1000)  # still don't get its function, but replace with variables

            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write(score_announcement.format(score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

SnakeGame.mainloop()
