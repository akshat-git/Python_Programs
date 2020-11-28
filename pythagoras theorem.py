import math
while True:
    p = int(input("Input a random number: "))
    q = int(input("Input a random number: "))

    tri = []
    tri.append(abs((p**2)-(q**2)))
    tri.append(2*p*q)
    tri.append((p**2)+(q**2))
    print(tri)

    a = tri[0]*10
    b = tri[1]*10
    c = tri[2]*10
    '''
import turtle
mypen = turtle.Pen()
mypen.fillcolor("red")
mypen.begin_fill()
mypen.goto(0,a)
mypen.goto(b,0)
mypen.home()
mypen.end_fill()
'''
    
