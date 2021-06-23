reglist = [24.0, 51.0, 46.0, 47.0, 25.0, 93.0, 140.0, 157.0, 64.0, 160.0, 142.0, 216.0, 142.0, 216.0, 68.0, 233.0, 127.0, 108.0, 75.0, 25.0, -28.0, 156.0, 8.0, 199.0, 92.0, 229.0, 108.0, 248.0, 198.0, 263.0, 202.0, 263.0, 190.0, 207.0, 145.0, 173.0, 0.0, 88.0, -60.0, 99.0, 1.0, 64.0, 44.0, -13.0, -60.0, 5.0, -92.0, 22.0, -97.0, -101.0, -131.0, -55.0, -183.0, -113.0, -56.0, -109.0, -62.0, -36.0, 14.0, -43.0, -168.0, -75.0, -232.0, -104.0, -214.0, -141.0, -208.0, -193.0, -102.0, -139.0, -143.0, -188.0, -305.0, -237.0, -221.0, -216.0, -190.0, -230.0]
checklen = int(len(reglist)/2)
lowres = 0
residsets = {}
unit = 30
for j in range(10000):
    newresid = 0
    for i in range(checklen):
        coorset = []
        coorset.append(reglist[(i*2)])
        coorset.append(reglist[((i*2)+1)])
        resid = (coorset[1]-((j/1000)*coorset[0]))**2
        newresid = newresid+resid
    residsets[(j/1000)] = newresid
lowres = min(residsets, key=residsets.get)
print(lowres)



import turtle
pen = turtle.Pen()
pen.pensize(2)
turtle.ht()
turtle.tracer(0,0)
turtle.ht()
for i in range(checklen):
    coorset = []
    coorset.append(reglist[(i*2)])
    coorset.append(reglist[((i*2)+1)])
    pen.penup()
    pen.goto(coorset[0],coorset[1])
    pen.pendown()
    pen.circle(1.5)
pen.penup()
pen.color('blue')
for i in range(-400,400):
    pen.goto(i,lowres*i)
    pen.pendown()
pen.home()
pen.color("black")
turtle.tracer(1000,1000)
pen.pendown()
from math import *
def axisarrows():
    pen.pendown()
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
    pen.pensize(1)
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
    makegraph()


unitdraw()
turtle.tracer(1000,1000)
    
    

    
    
