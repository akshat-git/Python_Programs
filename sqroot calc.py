from math import *
def sqroot(x):
    z = 2
    a = 0
    while (z**2)<(x):
        if (x % (z**2)) == 0:
            a = str(z)+" ~/"+str(x/(z**2))
        z = z+1
    if a == 0:
        a = "~/"+str(x)
    if x == 0:
        a = ""
    return a
while True:
    co = float(input("Coefficient: "))
    y = float(input("C: "))
    sqr = (co/2)**2
    left = str(-1*sqrt(sqr))
    right = str(sqroot(sqr-y))+" "+left
    print("x =",right)



            
        
        

