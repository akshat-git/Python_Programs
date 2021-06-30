print("    ___C______D___")
print(" C |  3,3    0,4  ")
print(" D |  4,0    1,1  ")
triggered = False
point1 = 0
point2 = 0
while True:
    userinput = input("Comply or Defect:  ")
    pcinput = ""
    if triggered == True:
        pcinput ="D"
    if triggered == False and pcinput != "D":
        pcinput = "C"
    if triggered == False and userinput == "D":
        triggered = True

    if pcinput == "C" and userinput == "C":
        point1 = point1+3
        point2 = point2+3
    if pcinput == "D"and userinput == "D":
        point1 = point1+1
        point2 = point2+1
    if pcinput == "C" and userinput == "D":
        point1 = point1+0
        point2 = point2+4
    if pcinput == "D" and userinput == "C":
        point1 = point1+4
        point2 = point2+0
    else:
        pass
    print("Computer:",point1)
    print("Human:",point2)


    



    
