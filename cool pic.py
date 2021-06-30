import turtle
pen = turtle.Pen()
x = 100
pen.ht()
pen.speed(10)
pen.home()
pen.penup()
pen.bk(150)
pen.rt(90)
pen.fd(10)
pen.lt(180)
pen.pendown()
for i in range(1000):
    pen.rt(10000/(9*x))
    for i in range(4):
        pen.fd(3*x)
        pen.rt(90)
    pen.lt(10000/(18*x))
    pen.fd(x/15)
    x = x*0.999
    
    
    
        
