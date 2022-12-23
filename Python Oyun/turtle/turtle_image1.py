import turtle

screen = turtle.Screen()

# resimler gif olmalı
image = "kurt.gif"

# add the shape first then set the turtle shape
screen.addshape(image)
turtle.shape(image)

screen.setup(800, 614)

#screen.bgcolor("lightblue")
screen.bgpic("nehir.gif")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Right")
screen.onkey(backward, "Left")
screen.onkey(left, "Up")
screen.onkey(right, "Down")
screen.listen()

input()
