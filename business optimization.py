
while True:
    x = ""
    y = ""
    print("Cost: C")
    print("Expo: B")
    c = float(input(" Enter C: "))
    b = float(input(" Enter B: "))
    popt = c*b/(b+1)
    i = 0
    x = str(c*b)
    y = str(b+1)
    done = False
    if popt%1 != 0:
        a = popt*b+1
        popt = str(x+" / "+y)
        x = str(c*b)
        while i < 20 and done == False:
            i = i+1
            if (((b+1)*i) % 1) == 0:
                x = str((c*b)*i)
                done = True
                x = str(float(x)*i)
        if y[0] == "-":
            x = str(float(x*(-1)))
            y = str(float(y*(-1)))
            popt = str(x+" / "+y)
                
    string = [float(x),float(y)]
    integer = 0
    mixed = ""
    while string[0] > string[1]:
        integer = integer+1
        string[0] = string[0]-string[1]
    mixed = str(integer)+" "+str(x)+"/"+str(y)
        
    print(" Optimal Price:",mixed)
    print("")
    
