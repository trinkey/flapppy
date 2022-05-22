# Use the below variable to change the framerate (NOTICE - MESSES WITH GRAVITY + SPEED) [RECCOMMENDED (default) FRAMERATE: 30]
framerate = 30 

import turtle, time, math
from random import randint as r

screen = turtle.Screen()
screen.tracer(0)
screen.setup(1000, 800)
screen.bgcolor("#333333")

screen.addshape("fbicons/fbpipe.gif")
screen.addshape("fbicons/fbdown2.gif")
screen.addshape("fbicons/fbdown1.gif")
screen.addshape("fbicons/fbstraight.gif")
screen.addshape("fbicons/fbup2.gif")
screen.addshape("fbicons/fbup1.gif")

pipe1 = turtle.Turtle()
pipe2 = turtle.Turtle()
pipe3 = turtle.Turtle()
pipe4 = turtle.Turtle()
pipe5 = turtle.Turtle()
bird = turtle.Turtle()

pipe1.shape("fbicons/fbpipe.gif")
pipe2.shape("fbicons/fbpipe.gif")
pipe3.shape("fbicons/fbpipe.gif")
pipe4.shape("fbicons/fbpipe.gif")
pipe5.shape("fbicons/fbpipe.gif")
bird.shape("fbicons/fbstraight.gif")

pipe1.hideturtle()
pipe2.hideturtle()
pipe3.hideturtle()
pipe4.hideturtle()
pipe5.hideturtle()

pipe1.pu()
pipe2.pu()
pipe3.pu()
pipe4.pu()
pipe5.pu()

bird.hideturtle()
bird.pu()
bird.speed(0)
bird.goto(-200, 0)
bird.showturtle()
bird.color("black")

screen.bgpic("fbicons/fbbackground.gif")

def newGameStart(t = 1):
    global bird, pipe1, pipe2, pipe3, pipe4, pipe5, screen, p1y, p2y, p3y, p4y, p5y
    if t == 1:
        bird.goto(0, -150)
        bird.clear()
        try:
            bird.write("Press Space to start!", align = "center", font = ["04b_19", 50, "normal"])
        except:
            bird.write("Press Space to start!", align = "center", font = ["Arial", 50, "normal"])
        bird.goto(-200, 0)
    pipe1.goto(600, p1y)
    pipe2.goto(900, p2y)
    pipe3.goto(1200, p3y)
    pipe4.goto(1500, p4y)
    pipe5.goto(1800, p5y)
    pipe1.showturtle()
    pipe2.showturtle()
    pipe3.showturtle()
    pipe4.showturtle()
    pipe5.showturtle()

def resetRandoms(which = 0):
    global p1y, p2y, p3y, p4y, p5y, pipe1, pipe2, pipe3, pipe4, pipe5
    p1y, p2y, p3y, p4y, p5y = r(-250, 250), r(-250, 250), r(-250, 250), r(-250, 250), r(-250, 250)
    if which == 0:
        p1y, p2y, p3y, p4y, p5y = r(-250, 250), r(-250, 250), r(-250, 250), r(-250, 250), r(-250, 250)
        pipe1.goto(pipe1.xcor(), p1y)
        pipe2.goto(pipe2.xcor(), p2y)
        pipe3.goto(pipe3.xcor(), p3y)
        pipe4.goto(pipe4.xcor(), p4y)
        pipe5.goto(pipe5.xcor(), p5y)
    elif which == 1:
        p1y = r(-250, 250)
        pipe1.goto(pipe1.xcor(), p1y)
    elif which == 2:
        p2y = r(-250, 250)
        pipe2.goto(pipe2.xcor(), p2y)
    elif which == 3:
        p3y = r(-250, 250)
        pipe3.goto(pipe3.xcor(), p3y)
    elif which == 4:
        p4y = r(-250, 250)
        pipe4.goto(pipe4.xcor(), p4y)
    elif which == 5:
        p5y = r(-250, 250)
        pipe5.goto(pipe5.xcor(), p5y)

def pipeMovement(sped = 1):
    global pipe1, pipe2, pipe3, pipe4, pipe5, screen, checkPipeMoveBack, framerate
    m = 450 * sped / framerate
    pipe1.goto(pipe1.xcor() - m, pipe1.ycor())
    pipe2.goto(pipe2.xcor() - m, pipe2.ycor())
    pipe3.goto(pipe3.xcor() - m, pipe3.ycor())
    pipe4.goto(pipe4.xcor() - m, pipe4.ycor())
    pipe5.goto(pipe5.xcor() - m, pipe5.ycor())
    checkPipeMoveBack()

def die():
    global screen
    screen.bye()

def jump(x = 0, y = 0):
    global birdvelocity, start, bird, framerate
    if start == 0:
        start = 1
        bird.clear()
    birdvelocity = 1440 / framerate

def gravityTime():
    global birdvelocity, bird, framerate
    if birdvelocity >= -1.6 * framerate:
        birdvelocity -= 240 / framerate
    bird.goto(bird.xcor(), bird.ycor() + birdvelocity)

def birdIconChange():
    global bird, birdvelocity
    if birdvelocity >= 10:
        if birdvelocity >= 25:
            bird.shape("fbicons/fbup2.gif")
        else:
            bird.shape("fbicons/fbup1.gif")
    elif birdvelocity <= -10:
        if birdvelocity >= -25:
            bird.shape("fbicons/fbdown1.gif")
        else:
            bird.shape("fbicons/fbdown2.gif")
    else:
        bird.shape("fbicons/fbstraight.gif")

def checkPipeMoveBack():
    global pipe1, pipe2, pipe3, pipe4, pipe5, resetRandoms
    if pipe1.xcor() <= -600:
        pipe1.goto(pipe1.xcor() + 1500, pipe1.ycor())
        resetRandoms(1)
    if pipe2.xcor() <= -600:
        pipe2.goto(pipe2.xcor() + 1500, pipe2.ycor())
        resetRandoms(2)
    if pipe3.xcor() <= -600:
        pipe3.goto(pipe3.xcor() + 1500, pipe3.ycor())
        resetRandoms(3)
    if pipe4.xcor() <= -600:
        pipe4.goto(pipe4.xcor() + 1500, pipe4.ycor())
        resetRandoms(4)
    if pipe5.xcor() <= -600:
        pipe5.goto(pipe5.xcor() + 1500, pipe5.ycor())
        resetRandoms(5)

def birddie():
    global bird, pipe1, pipe2, pipe3, pipe4, pipe5, start, birdvelocity, newGameStart, score
    bird.goto(0, -150)
    birdvelocity = 0
    start = 0
    try:
        bird.write("You died! Oh no!", align = "center", font = ["04b_19", 50, "normal"])
    except:
        bird.write("You died! Oh no!", align = "center", font = ["Arial", 50, "normal"])
    bird.goto(0, -175)
    try:
        bird.write("Press space to play again!", align = "center", font = ["04b_19", 15, "normal"])
    except:
        bird.write("Press space to play again!", align = "center", font = ["Arial", 15, "normal"])
    bird.goto(0, -200)
    m = "Score: " + str(score)
    try:
        bird.write(m, align = "center", font = ["04b_19", 15, "normal"])
    except:
        bird.write(m, align = "center", font = ["Arial", 15, "normal"])
    bird.goto(-200, 0)
    bird.shape("fbicons/fbstraight.gif")
    newGameStart(0)
    score = 0

def checkIfDie():
    global bird, birddie, pipe1, pipe2, pipe3, pipe4, pipe5, previous, score
    if bird.ycor() <= -360:
        birddie()
    if pipe1.xcor() >= -250 and pipe1.xcor() <= -150:
        if previous != 1:
            previous = 1
            score += 1
        if pipe1.ycor() + 125 <= bird.ycor() or pipe1.ycor() - 125 >= bird.ycor():
            birddie()
    if pipe2.xcor() >= -250 and pipe2.xcor() <= -150:
        if previous != 2:
            previous = 2
            score += 1
        if pipe2.ycor() + 125 <= bird.ycor() or pipe2.ycor() - 125 >= bird.ycor():
            birddie()
    if pipe3.xcor() >= -250 and pipe3.xcor() <= -150:
        if previous != 3:
            previous = 3
            score += 1
        if pipe3.ycor() + 125 <= bird.ycor() or pipe3.ycor() - 125 >= bird.ycor():
            birddie()
    if pipe4.xcor() >= -250 and pipe4.xcor() <= -150:
        if previous != 4:
            previous = 4
            score += 1
        if pipe4.ycor() + 125 <= bird.ycor() or pipe4.ycor() - 125 >= bird.ycor():
            birddie()
    if pipe5.xcor() >= -250 and pipe5.xcor() <= -150:
        if previous != 5:
            previous = 5
            score += 1
        if pipe5.ycor() + 125 <= bird.ycor() or pipe5.ycor() - 125 >= bird.ycor():
            birddie()

screen.onkeypress(die, "Return")
screen.onkeypress(jump, "space")
screen.onclick(jump)
screen.listen()

start = 0
birdvelocity = 0
previous = 5
score = 0

resetRandoms()
newGameStart()

while True:
    if start != 0:
        pipeMovement()
        gravityTime()
        birdIconChange()
        checkIfDie()
    screen.update()
    time.sleep(1 / framerate)