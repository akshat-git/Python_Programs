import numpy as np

def equsplit(equ):
    coeffstr = equ.split("=")[0]
    constant = float(equ.split("=")[1])
    x = 1
    y = 1
    coeffstr = coeffstr.split("x")
    x = coeffstr[0]
    y = coeffstr[1][:-1]
    if x == "":
        x = 1.0
    elif x == "-":
        x = -1.0
    else:
        x = float(x)
    if y == "" or y == "+":
        y = 1.0
    elif y == "-":
        y = -1.0
    else:
        y = float(y)
    
    return (x,y,constant)

class SystemOfEquations:
    def __init__(self, equ1, equ2):
        self.equ1 = equ1.replace(" ","")
        self.equ2 = equ2.replace(" ","")
        self.inputs1 = equsplit(self.equ1)
        self.inputs2 = equsplit(self.equ2)
        self.solution = SystemOfEquations.solve(self.inputs1, self.inputs2)

    def getequ(self):
        return (self.equ1,self.equ2)
    
    def solve(equinput1, equinput2):
        coeff = np.array([[equinput1[0], equinput1[1]],
                                 [equinput2[0], equinput2[1]]])
        div = False
        nosol = False
        det = equinput1[0]*equinput2[1]-equinput1[1]*equinput2[0]
        if det == 0:
            nosol = True
        if det in [1,2,5,10,-1,-2,-5,-10]:
            div = True
        ainv = np.array([[equinput2[1], -1*equinput1[1]],
                               [-1*equinput2[0], equinput1[0]]])
        const = np.array([equinput1[2], equinput2[2]])
        solution = list(ainv @ const)
        for i in range(len(solution)):
            if div and not nosol:
                solution[i] = solution[i]/det
            elif not nosol:
                solution[i] = str(solution[i])+"/"+str(det)
            else:
                solution[i] = "No Solutions"
        return "x = "+str(solution[0])+"; y = "+str(solution[1])

    def __str__(self):
        return self.solution


#Use input block below or directly input equations on line 52
'''
input_equation1 = input("Equation 1: ")
input_equation2 = input("Equation 2: ")
'''
system = SystemOfEquations("2x + 3y = 5", "6x + 7y = 6")
print(system)

