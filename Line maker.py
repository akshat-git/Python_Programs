import turtle
import math
pen = turtle.Pen()
pen.speed(10)
slope = (turtle.numinput("What is the slope of your line? ","Slope entry:"))-0.5
intercept = turtle.numinput("What is the y-intercept of your line? ","Y-intercept:")
unit_input = float(turtle.numinput("What is the unit?","Unit entry:"))
unit = (400/unit_input)+1
letterunit = unit*0.5
'''
def axisname():
    pen.pensize(5)
    pen.fillcolor("white")
    pen.penup()
    pen.lt(90)
    pen.fd(letterunit*1.8)
    pen.begin_fill()
    for i in range (4):
        pen.fd(letterunit*1.2)
        pen.rt(90)
    pen.end_fill()
    pen.rt(90)
    pen.fd(letterunit*0.2)
    pen.lt(90)
    pen.fd(letterunit*0.2)
    pen.pendown()
    pen.rt(45)
    pen.pensize(3)
    pen.fd(letterunit)
    pen.bk(letterunit)
    pen.penup()
    pen.rt(45)
    pen.fd(letterunit*0.73)
    pen.lt(135)
    pen.pendown()
    pen.fd(letterunit)
    pen.bk(letterunit)
    pen.penup()
    pen.rt(135)
    pen.bk(letterunit)
    pen.lt(90)
    pen.pensize(7)
    
    pen.bk(letterunit*2)
    pen.rt(90)
    pen.pendown()

def axisname2():
    pen.pensize(5)
    pen.fillcolor("white")
    pen.penup()
    pen.lt(90)
    pen.fd(letterunit*1.75)
    pen.begin_fill()
    pen.lt(90)
    for i in range (4):
        pen.fd(letterunit*1.3)
        pen.rt(90)
    pen.end_fill()
    pen.fd(letterunit*0.25)
    pen.pendown()
    pen.rt(35)
    pen.pensize(3)
    pen.fd(letterunit*1.1)
    pen.bk(letterunit*1.1)
    pen.penup()
    pen.rt(55)
    pen.fd(letterunit*0.66)
    pen.lt(125)
    pen.fd(letterunit*0.55)
    pen.pendown()
    pen.fd(letterunit*0.55)
    pen.penup()
    pen.bk(letterunit*1.1)
    pen.rt(125)
    pen.bk(letterunit*0.66)
    pen.pensize(7)
    
    pen.bk(letterunit*1.75)
    pen.rt(90)
    pen.pendown()
'''
#make the axis lines
def makegraph():
    pen.home()
    pen.pensize(7)
    pen.fd(400)
    pen.bk(750)
    #axisname()
    pen.pensize(7)
    pen.bk(50)
    pen.fd(400)
    pen.home()
    pen.rt(90)
    pen.pensize(7)
    pen.fd(400)
    pen.bk(675)
    #axisname2()
    pen.pensize(7)
    pen.bk(125)
    pen.fd(400)
    

#plot the line
def plot():
    if slope < 1:
        degrees = 90-45*slope
    elif slope == 1:
        degrees = 45
    elif slope > 1:
        degrees = 45/slope

    pen.penup()
    pen.home()
    pen.pendown()
    pen.color("red")
    pen.pensize(8)
    pen.penup()
    pen.lt(90)
    pen.fd(intercept*unit)
    pen.rt(degrees)
    pen.pendown()
    pen.fd(1200)
    pen.bk(2400)
    pen.fd(1200)
    pen.penup()
    pen.home()
    pen.pendown()

#make the background units
def unitdraw():

    pen.pensize(1)
    for j in range (4):
        for i in range (math.floor(400/unit)):
            pen.penup()
            pen.fd(unit)
            pen.pendown()
            pen.rt(90)
            pen.fd(400)
            pen.bk(800)
            pen.fd(400)
            pen.lt(90)

        pen.home()
        pen.lt(90*(j+1))
        
        


unitdraw()
makegraph()
plot()
pen.ht()
print("BYE !!!")
