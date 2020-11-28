#make a python drawing
import turtle
#variables
x1 = int(turtle.numinput("DRAWING SIZE","What size do you want your drawing to be"))
x = x1*0.98
mypen = turtle.Pen()
x2 = x*1.25
eye = 0.2*x
#bluepart
mypen.color("blue")
mypen.fillcolor("blue")
mypen.begin_fill()
mypen.circle(x,180)
mypen.fd(x)
mypen.circle(x,75)
mypen.circle(x/5,105)
mypen.rt(180)
mypen.circle(x,180)
mypen.lt(90)
mypen.penup()
mypen.fd(x)
mypen.rt(90)
mypen.fd(x)
mypen.rt(180)
mypen.pendown()
mypen.bk(x*0.9)
mypen.fd(x*0.9)
mypen.circle(x,90)
mypen.penup()
mypen.rt(180)
mypen.fd(x)
mypen.rt(90)
mypen.fd(x)
mypen.rt(180)
mypen.pendown()
mypen.end_fill()

#gold part
mypen.color("gold")
mypen.fillcolor("gold")
mypen.begin_fill()
mypen.circle(x,180)
mypen.fd(x)
mypen.circle(x,75)
mypen.circle(x/5,105)
mypen.rt(180)

mypen.circle(x,180)
mypen.lt(90)
mypen.penup()
mypen.fd(x)
mypen.rt(90)
mypen.fd(x)
mypen.rt(180)
mypen.pendown()
mypen.bk(x*0.9)
mypen.fd(x*0.9)
mypen.circle(x,90)
mypen.penup()
mypen.rt(180)
mypen.fd(x)
mypen.rt(90)
mypen.pendown()
mypen.end_fill()

#prepare for eyes
mypen.color("white")
mypen.fillcolor()
mypen.penup()

#eye1
mypen.color("white")
mypen.goto(x2*0.33,-(x2))
mypen.pendown()
mypen.begin_fill()
mypen.circle(eye,360)
mypen.end_fill()

#eye2
mypen.color("white")
mypen.begin_fill()
mypen.penup()
mypen.goto(-x2,x2*1.35)
mypen.pendown()
mypen.circle(eye,360)
mypen.end_fill()

#necklines
mypen.color("white")
mypen.penup()
mypen.home()
mypen.lt(90)
mypen.fd(x)
mypen.lt(90)
mypen.fd(x/2)
mypen.pendown()
mypen.fd(1.5*x)
mypen.penup()
mypen.home()

mypen.bk(x*0.9)
mypen.rt(90)
mypen.fd(x)
mypen.lt(90)
mypen.fd(x/2)
mypen.pendown()
mypen.fd(1.5*x)
mypen.penup()
mypen.home()
mypen.ht()
    

