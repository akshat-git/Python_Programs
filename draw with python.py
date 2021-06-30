import turtle
pen = turtle.Pen()
wn = turtle.Screen()
pen.lt(90)
pen.speed(10)
def forward():
    pen.forward(10)
def back():
    pen.backward(10)
def fdx(x):
    pen.forward(x)
def bkx(x):
    pen.backward(x)
def right():
    pen.right(5)
def right90():
    pen.right(90)
def left():
    pen.left(5)
def left90():
    pen.left(90)
def penup():
    pen.penup()
def pendown():
    pen.pendown()
def penmode():
    pen.color("black")
def erasemode():
    pen.color("white")
def circ():
    for i in range(36):
        forward()
        left()
        left()
def pattern():
    pendown()
    for i in range(36):
        pen.fillcolor("black")
        for i in range(3):
            fdx(100)
            right90()
            fdx(100)
            left90()
        for i in range(10):
            left()
        fdx(100)
        bkx(100)
        for i in range(10):
            right()
        for i in range(3):
            right90()
            bkx(100)
            left90()
            bkx(100)
        right()
        pen.fillcolor("white")
        for i in range(3):
            fdx(100)
            right90()
            fdx(100)
            left90()
        for i in range(10):
            left()
        fdx(100)
        bkx(100)
        for i in range(10):
            right()
        for i in range(3):
            right90()
            bkx(100)
            left90()
            bkx(100)
        right()    
        
        
wn.listen()
wn.onkey(pattern, "a")
wn.onkey(forward, "Up")  
wn.onkey(back, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(penup, "u")
wn.onkey(pendown, "d")
wn.onkey(penmode, "p")
wn.onkey(erasemode, "e")
wn.onkey(circ, "c")



