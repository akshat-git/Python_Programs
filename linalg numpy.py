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
        const = np.array([equinput1[2], equinput2[2]])
        
        solution = np.linalg.solve(coeff, const)
        return "x = "+str(round(solution[0], 5))+"; y = "+str(round(solution[1], 5))

    def __str__(self):
        return self.solution


#Use input block below or directly input equations on line 52
'''
input_equation1 = input("Equation 1: ")
input_equation2 = input("Equation 2: ")
'''
system = SystemOfEquations("2x + 5y = 24", "-3x + y = -19")
print(system)
print(system.getequ())

