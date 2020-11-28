from math import *
real = True
def sqroot(b):
    real = True
    if b < 0:
        real = False
        b = b*(-1)
    if sqrt(b) % 1 == 0:
        if real == True:
            return sqrt(b)
        else:
            return str(sqrt(b))+" i"
    else:
        if real == True:
            return "-/"+str(b)
        else:
            return "-/"+str(b)+" i"
while True:
    co = float(input("Coefficient: "))
    y = float(input("C: "))
    left = (co/2)
    linear = str(left*(-1)) +" +- "+ sqroot((left**2) - y)
    print("x =",str(linear))
    
    



            
        
        

