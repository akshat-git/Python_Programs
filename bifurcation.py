import turtle
pen = turtle.Pen()
pen.ht()
turtle.tracer(0,0)
pen.pensize(3)
def plot(x,y):
    pen.ht()
    pen.goto(x,y)
    pen.pendown()
    pen.circle(1)
    
def equ(x):
    return (rate*x*(1-x))
pen.clear()
rate = float(turtle.textinput("","Rate: "))
xlist = []
xlist.append(0.4)
for i in range(45):
    x = xlist[i]*rate*(1-xlist[i])
    xlist.append(round(x,4))
pen.penup()
for i in range(45):
    plot(i*15-350,xlist[i]*300-175)
     
    
