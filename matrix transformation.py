import numpy as np
import turtle
from math import *


root2 = 2**.5
transformation = np.array([[-.25, -.75],
                                          [.75, -.25]])
shape = [[-6, -6, 6, 6],
              [-2, 6, 2, -6]]
square = [[2,-2, -2, 2],
              [2, 2, -2, -2]]
wheel = [[1, -1, -1-root2, -1-root2, -1, 1, 1+root2 ,1+root2],
         [1+root2, 1+root2, 1, -1, -1-root2, -1-root2, -1, 1]]
polygon = np.array(shape)
polygon = polygon*1
pointcount = len(polygon[0])
pen = turtle.Pen()
pen.ht()
pen.pensize(1)
pen.speed(10)
unit = 20

for j in range(4):
    for i in range(10):
        pen.fd(unit)
        pen.lt(90)
        pen.fd(unit*10)
        pen.bk(unit*20)
        pen.fd(unit*10)
        pen.rt(90)
    pen.pensize(3)
    pen.bk(unit*10)
    pen.pensize(1)
    pen.rt(90)

    
pen.pensize(3)
transformed = polygon

#while True:
pen.color("blue")
pen.penup()
for i in range(pointcount+1):
    pen.goto(transformed[0,i % pointcount]*unit,transformed[1,i % pointcount]*unit)
    pen.pendown()
transformed = transformation @ transformed
pen.color("red")

pen.penup()
pen.home()
for i in range(pointcount+1):
    pen.goto(transformed[0,i % pointcount]*unit,transformed[1,i % pointcount]*unit)
    pen.pendown()
    '''
    turtle.clearscreen()
    transformed = transformation @ transformed
    '''

    
    
    
    
        
        
