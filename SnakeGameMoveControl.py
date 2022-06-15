import turtle

turtles = turtle.Screen()
head = turtle.Turtle()

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