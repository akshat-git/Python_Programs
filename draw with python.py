import turtle
pen = turtle.Pen()
wn = turtle.Screen()
pen.lt(90)
pen.speed(10)
def forward():
    pen.forward(10)
def back():
    pen.backward(10)
def right():
    pen.right(5)
def left():
    pen.left(5)
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
    for i in range(36):
        circ()
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



