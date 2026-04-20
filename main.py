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

player = Turtle()
player.color("red")
player.shape("circle")
player.shapesize(1.5)
player.up()
player.hideturtle()

# List of turtle objects: each {'pos': [x,y], 'dir': angle, 'active': bool}
turtles = [{'pos': [0, 0], 'dir': random.randint(0, 360), 'active': True}]

speed = 5

key_pressed = { "a" : False, "d" : False, "space" : False}





def bounce(turtle_pos, direction, pen, turtles):
    
    new_dir = direction
    if turtle_pos[0] > 290:
        new_dir = 180 - direction
        if pen == "turtle":
            turtles.append({'pos': [turtle_pos[0] - 5, turtle_pos[1]], 'dir': random.randint(91, 179), 'active': True})
    elif turtle_pos[0] < -290:
        new_dir = 0 + (180 - direction)
        if pen == "turtle":
            turtles.append({'pos': [turtle_pos[0] + 5, turtle_pos[1]], 'dir': random.randint(91, 179) + 180, 'active': True})
    elif turtle_pos[1] > 290:
        new_dir = 270 + (90 - direction)
        if pen == "turtle":
            turtles.append({'pos': [turtle_pos[0], turtle_pos[1] - 5], 'dir': random.randint(181, 359), 'active': True})
    elif turtle_pos[1] < -290:
        new_dir = 90 + (270 - direction)
        if pen == "turtle":
            turtles.append({'pos': [turtle_pos[0], turtle_pos[1] + 5], 'dir': random.randint(1, 179), 'active': True})

    return new_dir


def turtle_run(turtle_obj):
    if not turtle_obj['active']:
        return
    
    if key_pressed.get("space") and player.distance(turtle_obj['pos'][0], turtle_obj['pos'][1]) < 20:
        turtle_obj['active'] = False
        return
    
    turtle_pos = turtle_obj['pos']

    turtle.goto(turtle_pos[0], turtle_pos[1])
    
    if turtle_pos[0] >= 290 or turtle_pos[0] <= -290 or turtle_pos[1] >= 290 or turtle_pos[1] <= -290:
        turtle_obj['dir'] = bounce(turtle_pos, turtle_obj['dir'], "turtle", turtles)
    turtle.setheading(turtle_obj['dir'])
    turtle.forward(speed)
        
    turtle_obj['pos'] = [turtle.xcor(), turtle.ycor()]
    
    turtle.stamp()
    
def key_down(key):
    global keys_pressed
    key_pressed[key] = True

def key_up(key):
    global keys_pressed
    key_pressed[key] = False

def player_movement():
    global player

    turtle_pos = [player.xcor(), player.ycor()]
    if turtle_pos[0] >= 290 or turtle_pos[0] <= -290 or turtle_pos[1] >= 290 or turtle_pos[1] <= -290:
        player.setheading(bounce(turtle_pos, player.heading(), "player", turtles))

    for key, on in key_pressed.items():
        
        if on:
            
            
            if key == "a":
                player.left(2.5)
            elif key == "d":
                player.right(2.5)
                
    player.forward(speed)
    player.stamp()
    



def main():


    pen.up()
    pen.goto(-300,300)
    pen.down()
    pen.goto(-300,-300)
    pen.goto(300,-300)
    pen.goto(300,300)
    pen.goto(-300,300)
    pen.up()
    pen.home()


    window.tracer(0)
    while True:
        for turtle_obj in turtles:
            turtle_run(turtle_obj)
        if key_pressed.get("space"):
            player_movement()
        window.update()
        turtle.clear()
        player.clear()





window.listen()


window.onkeypress(lambda: key_down("space"), "space")

window.onkeypress(lambda: key_down("a"), "a")
window.onkeyrelease(lambda: key_up("a"), "a")
window.onkeypress(lambda: key_down("d"), "d")
window.onkeyrelease(lambda: key_up("d"), "d")


main()
window.exitonclick()