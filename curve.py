import turtle
pen = turtle.Pen()
x = 270
pen.speed(10)
pen.home()
pen.penup()
pen.bk(150)
pen.rt(90)
pen.fd(150)
pen.lt(180)
pen.pendown()
pen.fd(270)
pen.bk(270)
pen.rt(90)
pen.fd(270)
pen.bk(270)
for i in range(90):
    pen.fd(5)

    pen.lt(90+(i))
    pen.fd(270)
    pen.bk(270)

    pen.rt(90+(i))
