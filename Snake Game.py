import turtle
import time
import random

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

# move control

def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"


def goRight():
    if head.direction != "left":
        head.direction = "right"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

def move():
    # y axis 
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    # x axis
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
turtles.listen()
turtles.onkeypress(goUp,"w")
turtles.onkeypress(goDown,"s")
turtles.onkeypress(goRight,"d")
turtles.onkeypress(goLeft,"a")

