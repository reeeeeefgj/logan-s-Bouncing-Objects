import random
from turtle import *

window = Screen()
window.setup(900,900)
window.bgcolor("black")

turtle = Turtle()
turtle.color("white")
turtle.shape("square")
turtle.up()
pen = Turtle()
pen.hideturtle()
pen.color("white")
pen.up()
pen.goto(-300,300)
pen.down()
pen.goto(-300,-300)
pen.goto(300,-300)
pen.goto(300,300)
pen.goto(-300,300)
pen.up()
pen.home()
turtle_poition = [0,0]
#                 x y
speed = 10
direction = random.randint(0,360)
def bounce(turtle_poition):
    global direction
    
    if turtle_poition[0] > 290:
        direction = 180 -  direction
    elif turtle_poition[0] < -290:
        direction = 0 + (180 - direction)
    elif turtle_poition[1] > 290: 
        direction = 270 + (90 - direction)
    elif turtle_poition[1] < -290:
        direction = 90 + (270 - direction)

        
   
def main(turtle_poition):
    turtle.up()
    window.tracer(0)

    while True:
        turtle.clear()
        turtle_poition[0] = turtle.xcor()
        turtle_poition[1] = turtle.ycor()
        if turtle_poition[0] >= 290 or turtle_poition[0] <= -290 or turtle_poition[1] >= 290 or turtle_poition[1] <= -290:
            bounce(turtle_poition)
        turtle.setheading(direction)
        turtle.forward(speed)
        turtle.setheading(0)
        turtle.stamp()
        window.update()
        

direction = random.randint(0,360)
main(turtle_poition)
mainloop()