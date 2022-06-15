import turtle
import time
import random
import SnakeGameMoveControl

delay = 0.1
score = 0
high_score = 0

# creating window screen
turtles = turtle.Screen()
turtles.title("贪吃蛇 Snake Game")
turtles.bgcolor("blue")

# width and height
turtle.setup(width=600, height=600)
turtle.tracer(0)

# snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"

# food
food = turtle.Turtle()
colors = random.choice(["red","yellow","green"])
food.speed(0)
food.shape("circle")
food.color(colors)
food.penup()
food.goto(0,100)

# score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High Score : 0", align="center", font=("candara",24,"bold"))

# Gameplay
segments = []
while True:
    turtles.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: # add a map size customized by player
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        colors = random.choice(["red","blue","gree"])
        shapes = random.choice(["square","circle"])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0 # reset score
        delay = 0.1 
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score,high_score),align="center", font=("candara", 24, "bold"))
    
    # ate food
    if head.distance(food) < 20:
        x = random.randint(-270,270) # map size here again
        y = random.randint(-270,270)
        food.goto(x,y)

        #Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        


