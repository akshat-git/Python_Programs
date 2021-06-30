while True:
    xco = int(input("x: "))
    yco = int(input("y: "))
    integer = int(input("int: "))*-1
    if integer < 0:
        print("y =  (",xco,"x - ",abs(integer),") / ",-1*yco,sep = "")
    else:
        print("y =  (",xco,"x + ",integer,") / ",-1*yco,sep = "")

