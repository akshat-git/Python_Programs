import turtle
import math

# Take user input
makelineinput = turtle.textinput("Line options","Make a line or not? Yes or No:  ")
makesineinput = turtle.textinput("Sinewave options","Make a sine wave or not? Yes or No:  ")
makecosineinput = turtle.textinput("Cosinewave options","Make a cosine wave or not? Yes or No:  ")
makesine = True
makeline = True
makecosine = True
screen = turtle.Screen()
if str(makelineinput) == "Yes":
    makeline = True
elif str(makelineinput) == "No":
    makeline = False

if str(makesineinput) == "No":
    makesine = False  
elif str(makesineinput) == "Yes":
    makesine = True

if str(makecosineinput) == "No":
    makecosine = False  
elif str(makecosineinput) == "Yes":
    makecosine = True

unit_input = turtle.numinput("Unit entry","What is the unit?  ")
unit = (400/unit_input)+1

pen = turtle.Pen()
pen.speed(10)


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
def unitdraw():
    pen.pensize(2)
    for j in range (4):
        for i in range (math.ceil(400/30)):
            pen.penup()
            pen.fd(unit)
            pen.pendown()
            pen.rt(90)
            pen.fd(408)
            pen.bk(816)
            pen.fd(408)
            pen.lt(90)

        pen.home()
        pen.lt(90*(j+1))
        
def makelineplot():
    if makeline == True:
        equ = turtle.textinput("","What is the equation? (mx + b) format: ")
        slope = ""
        interceptline = ""
        slopedone = False
        for i in range(len(equ)):
            if equ[i] != "x" and slopedone == False:
                slope = slope + equ[i]
            elif (equ[i] != "x" )and slopedone == True:
                interceptline = interceptline + equ[i]
            elif equ[i] == "x":
                slopedone = True
        slope = float(slope)
        interceptline = float(interceptline)  
        pen.color("blue")
        pen.pensize(4)
        pen.speed(10)
        pen.penup()
        pen.home()
        print(interceptline)
        for x in range(-400,401):
            pen.goto(x,(x * slope) + interceptline*unit)
            pen.pendown()
    else:
        print("No line drawn")

def makesineplot():
    if makesine == True:
        amp = turtle.numinput("Amplitude entry","Amplitude: ")*unit
        freq = turtle.numinput("Frequency entry","Frequency: ")
        pen.speed(10)
        pen.color("red")
        pen.penup()
        pen.home()
        pen.pensize(4)
        
        for x in range(-408,409):
            pen.goto(x, (amp * math.sin(x * freq * math.pi/180)))
            pen.pendown()
    else:
        print("No sine wave drawn")

def makecosineplot():
    if makecosine == True:
        amp = turtle.numinput("Amplitude entry","Amplitude: ")*unit
        freq = turtle.numinput("Frequency entry","Frequency: ")
        pen.speed(10)
        pen.color("green")
        pen.penup()
        pen.home()
        pen.pensize(4)
        
        for x in range(-408,409):
            pen.goto(x, (amp * math.cos(x * freq * math.pi/180)))
            pen.pendown()
    else:
        print("No cosine wave drawn")

def callfunc():
    
    unitdraw()
    makegraph()
    makelineplot()
    makesineplot()
    makecosineplot()
    
callfunc()
pen.ht()
screen.exitonclick()
