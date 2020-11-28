while True:
    subtr = False
    subint = 0
    equ = input("Equation input: ")
    ab = ""
    ay = ""
    bx = ""
    xy = ""
    equsplit = equ.split("+")

    ay = equsplit[1].split("a")
    bx = equsplit[2].split("b")
    if ay[0] == "":
        ay[0] = "1"
    if bx[0] == "":
        bx[0] = "1"
    ay = int(ay[0])
    bx = int(bx[0])
    xy = int(equsplit[3])
    if ay*bx != xy:
        subtr = True
        subint = (ay*bx)-xy
    if subtr != True:
        if ay>=0 and bx>=0:
            print("(a + ",bx,")(b + ",ay,")",sep = "")
        if ay<0 and bx>=0:
            print("(a + ",bx,")(b - ",-1*ay,")",sep = "")
        if ay>=0 and bx<0:
            print("(a - ",-1*bx,")(b + ",ay,")",sep = "")
        if ay<0 and bx<0:
            print("(a - ",-1*bx,")(b - ",-1*ay,")",sep = "")
    if subtr == True:
        if subint < 0:
            if ay>=0 and bx>=0:
                print("(a + ",bx,")(b + ",ay,")",subint, sep = "")
            if ay<0 and bx>=0:
                print("(a + ",bx,")(b - ",-1*ay,")",subint,sep = "")
            if ay>=0 and bx<0:
                print("(a - ",-1*bx,")(b + ",ay,")",subint,sep = "")
            if ay<0 and bx<0:
                print("(a - ",-1*bx,")(b - ",-1*ay,")",subint,sep = "")
        if subint > 0:
            if ay>=0 and bx>=0:
                print("(a + ",bx,")(b + ",ay,") +",subint,sep = "")
            if ay<0 and bx>=0:
                print("(a + ",bx,")(b - ",-1*ay,") +",subint,sep = "")
            if ay>=0 and bx<0:
                print("(a - ",-1*bx,")(b + ",ay,") +",subint,sep = "")
            if ay<0 and bx<0:
                print("(a - ",-1*bx,")(b - ",-1*ay,") +",subint,sep = "")
    
