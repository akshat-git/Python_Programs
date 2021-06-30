while True:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    m = (y2-y1)/(x2-x1)
    mstr = str(y2-y1)+"/"+str(x2-x1)
    b = y1-(x1*m)

    print("y = ",mstr,"x + (" ,b, ")",sep = "")
