print("")
print("Given equation in format |mult*x+y| (ineq.) z :")
print("")
import math
while True:
    xmultin = input("What is the multiplier for x? ")
    xmultin = xmultin.split("/")
    if len(xmultin) > 1:
        xmultin = float(xmultin[0])/float(xmultin[1])
    xmult = float(xmultin)

    var = input("What is the variable? ")
    
    yin = input("Y: ")
    yin = yin.split("/")
    if len(yin) > 1:
        yin = float(yin[0])/float(yin[1])
    y = float(yin)*-1
    
    ineq = input("What is the inequality ")
    
    zin = input("Z: ")
    zin = zin.split("/")
    if len(zin) > 1:
        zin = float(zin[0])/float(zin[1])
    z = float(zin)
    
    lower = (y-z)/xmult
    higher = (y+z)/xmult
    lower = round(lower,10)
    higher = round(higher,10)
    print("")
    if z < 0:
        print("No Solutions")
    else:
        if ineq == "=":
            print(var,"=",lower,",",var,"=",higher)
            if y == 0:
                print(var,"=",z/xmult)
                
        elif ineq == "<":
            print(lower,"<",var,"<",higher)
            if y == 0:
                print(var,"<",z/xmult)

        elif ineq == "<=":
            print(lower,"<=",var,"<=",higher)
            if y == 0:
                print(var,"<=",z/xmult)
                
        elif ineq == ">":
            print(var,"<",lower,",",var,">",higher)
                
        elif ineq == ">=":
            print(var,"<=",lower,",",var,">=",higher)
        else:
            print("Type either =,>,<,<=,or >=! ")
    print("")
    
