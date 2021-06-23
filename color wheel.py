import turtle
pen = turtle.Pen()
pen.speed(10)
for i in range(120):
    j = 255-i
    colors = [i,j,0]
    pen.pencolor()
    pen.fd(100)
    pen.bk(100)
    pen.rt(1)
