from math import *
import turtle
import time
import random
problemnum = input("What is the problem number: ")+")"
print("Maximize upcoming window for better effect")
time.sleep(2)
pen = turtle.Pen()
pen.speed(10)
unit = 30
pen.penup()
pen.goto(-480,350)
pen.pendown()
pen.write(problemnum, font = ('Comic Sans MS', 18, 'normal'))
pen.penup()
pen.home()
pen.pendown()
done = False
colors = ["red1","RoyalBlue","SpringGreen","turquoise1", "purple2"]
turtle.tracer(0,0)

def unitdraw():
    pen.pensize(2)
    for j in range (4):
        for i in range (ceil(400/30)):
            pen.penup()
            pen.fd(30)
            pen.pendown()
            pen.rt(90)
            pen.fd(420)
            pen.bk(840)
            pen.fd(420)
            pen.lt(90)

        pen.home()
        pen.lt(90*(j+1))
def axisarrows():
    pen.rt(30)
    pen.fd(unit*0.5)
    pen.bk(unit*0.5)
    pen.lt(60)
    pen.fd(unit*0.5)
    pen.bk(unit*0.5)
    pen.rt(30)
#make the axis lines
def makegraph():
    pen.home()
    pen.pensize(7)
    pen.fd(408)
    pen.rt(180)
    axisarrows()
    pen.rt(180)
    pen.bk(816)
    axisarrows()
    pen.fd(408)
    pen.rt(90)
    pen.pensize(7)
    pen.fd(408)
    pen.rt(180)
    axisarrows()
    pen.rt(180)
    pen.bk(816)
    axisarrows()
    pen.fd(408)
    pen.ht()

unitdraw()
pen.pendown()
makegraph()

def absval():
    pen.ht()
    time.sleep(2)
    equ = turtle.textinput("","Equation:")
    equ = equ.split("|")
    equ = equ[1:len(equ)-1]
    equ1 = equ[0]
    oper = equ[1]
    equ2 = equ[2]
    slope1 = ""
    interceptline1 = ""
    slopedone1 = False
    for i in range(len(equ1)):
        if equ1[i] != "x" and slopedone1 == False:
            slope1 = slope1 + equ1[i]
        elif (equ1[i] != "x" )and slopedone1 == True:
            interceptline1 = interceptline1 + equ1[i]
        elif equ1[i] == "x":
            slopedone1 = True
    if slope1 == "":
        slope1 = "1"
    if interceptline1 == "":
        interceptline1 = "0"
    slope1 = float(slope1)
    interceptline1 = float(interceptline1)  
    pen.color(random.choice(colors))
    pen.pensize(4)
    pen.speed(10)
    pen.penup()
    pen.home()

    slope2 = ""
    interceptline2 = ""
    slopedone2 = False
    for i in range(len(equ2)):
        if equ2[i] != "x" and slopedone2 == False:
            slope2 = slope2 + equ2[i]
        elif (equ2[i] != "x" )and slopedone2 == True:
            interceptline2 = interceptline2 + equ2[i]
        elif equ2[i] == "x":
            slopedone2 = True
    if slope2 == "":
        slope2 = "1"
    if interceptline2 == "":
        interceptline2 = "0"
    slope2 = float(slope2)
    interceptline2 = float(interceptline2)
    pen.pensize(4)
    pen.speed(10)
    pen.penup()
    pen.home()


    for x in range(-400,401):
        if oper == "+":
            pen.goto(x,abs((x * slope1) + interceptline1*30)+ abs((x * slope2) + interceptline2*30))
        if oper == "-":
            pen.goto(x,abs((x * slope1) + interceptline1*30)- abs((x * slope2) + interceptline2*30))
        pen.pendown()

while True:
    time.sleep(1)
    absval()

        

