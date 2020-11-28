equ = input("What is the equation? (mx + b) format: ")
slope = ""
intercept = ""
slopedone = False
for i in range(len(equ)):
    if equ[i] != "x" and slopedone == False:
        slope = slope + equ[i]
    elif (equ[i] != "x" )and slopedone == True:
        intercept = intercept + equ[i]
    elif equ[i] == "x":
        slopedone = True
slope = float(slope)
intercept = float(intercept)
        
