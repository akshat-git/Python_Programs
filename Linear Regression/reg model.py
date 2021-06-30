import turtle
import time
import math
reglist = []
slopelist = []
pen = turtle.Pen()
pen.ht()
pen.width(5)
turtle.tracer(0,0)
def get_mouse_click_coor(x, y):
    pen.penup()
    reglist.append(x)
    reglist.append(y)
    print(reglist)
    pen.goto(x,y)
    pen.pendown()
    pen.circle(1)
    slope = y/x
    slopelist.append(slope)        
        
        

turtle.onscreenclick(get_mouse_click_coor)



