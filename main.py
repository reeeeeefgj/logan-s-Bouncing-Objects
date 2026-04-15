import random
from turtle import *

window = Screen()
window.setup(900,900)
window.bgcolor("black")

turtle = Turtle()
turtle.color("white")
turtle.shape("circle")
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

#                 x y
poition = { 0: [0,0]}
directions = [random.randint(0,360)]



amount_turtle = 1
speed = 5
direction = random.randint(0,360)
def bounce(turtle_poition,direction):
    global amount_turtle, poition, directions
    
    if turtle_poition[0] > 290:
        direction = 180 - direction
        amount_turtle += 1
        poition[amount_turtle - 1] = [turtle_poition[0] - 5, turtle_poition[1]]
        directions.append(random.randint(91,179))
    elif turtle_poition[0] < -290:
        direction = 0 + (180 - direction)
        amount_turtle += 1
        poition[amount_turtle - 1] = [turtle_poition[0] + 5, turtle_poition[1]]
        directions.append(random.randint(91,179) + 180)
    elif turtle_poition[1] > 290:
        direction = 270 + (90 - direction)
        amount_turtle += 1
        poition[amount_turtle - 1] = [turtle_poition[0], turtle_poition[1] - 5]
        directions.append(random.randint(181,359))
    elif turtle_poition[1] < -290:
        direction = 90 + (270 - direction)
        amount_turtle += 1
        poition[amount_turtle - 1] = [turtle_poition[0], turtle_poition[1] + 5]
        directions.append(random.randint(1,179))

    return direction


def turtle_run(turtle_index):
    
    global directions, poition, turtle
    
    turtle_poition = poition.get(turtle_index)

    turtle.goto(turtle_poition[0], turtle_poition[1])
    
    if turtle_poition[0] >= 290 or turtle_poition[0] <= -290 or turtle_poition[1] >= 290 or turtle_poition[1] <= -290:
        directions[turtle_index] = bounce(turtle_poition, directions[turtle_index])
    turtle.setheading(directions[turtle_index])
    turtle.forward(speed)
        
    poition[turtle_index] = [turtle.xcor(), turtle.ycor()]
    turtle.stamp()
    
        

direction = random.randint(0,360)

def main():

    window.tracer(0)
    while True:
        for i in range(amount_turtle):
            turtle_run(i)
        window.update()
        turtle.clear()
main()
mainloop()