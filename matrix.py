import turtle

 

import random

 

turtle = turtle.Turtle()

 

turtle.speed("fastest")

 

turtle.lt(30)

 

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Dark Blue", "Purple"]

 

def gotostart():

 

    turtle.up()

 

    turtle.lt(90)

 

    turtle.fd(300)

 

    turtle.lt(90)

 

    turtle.fd(300)

 

    turtle.rt(180)

 

    turtle.down()

 

def square():

    turtle.begin_fill()

 

    for i in range(4):

 

        turtle.forward(30)

 

        turtle.right(90)

 

    turtle.end_fill()

 

def nextshape():

 


    turtle.up()

 

    turtle.fd(60)

 

    turtle.down()

 

def nextrow():

 

    turtle.up()

 

    turtle.bk(600)

 

    turtle.rt(90)

 

    turtle.fd(60)

 

    turtle.lt(90)

 

    turtle.down()

 

def grid():

 

    for i in range(10):

 

        for j in range(10):

 

            square()

 

            nextshape()

 

        nextrow()

 

        turtle.fillcolor(random.choice(colors))

 

gotostart()

 

for i in range(5):

 

    grid()

 

    turtle.lt(30)

 

    turtle.up()

 

    turtle.lt(60)

 

    turtle.fd(200)

 

    turtle.rt(60)

 

    turtle.down()
