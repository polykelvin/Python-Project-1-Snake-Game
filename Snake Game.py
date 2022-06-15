import turtle

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# creating window screen
turtles = turtle.Screen()
turtles.title("贪吃蛇")
turtles.bgcolor("blue")

# width and height
turtle.setup(width=500, height=500)
turtle.tracer()

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

turtle.done()