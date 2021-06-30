import numpy
import warnings
warnings. filterwarnings("ignore")
print("Equation 1: ")
cox1 = float(input("    Coeffiecient of x: "))
coy1 = float(input("    Coeffiecient of y: "))
right1 = float(input("    Answer: "))
print("Equation 2: ")
cox2 =  float(input("    Coeffiecient of x: "))
coy2 =  float(input("    Coeffiecient of y: "))
right2 = float(input("    Answer: "))

varlist = ["x =","y ="]


A = [[cox1, coy1],
     [cox2, coy2]]
B = [[right1],
     [right2]]
x = numpy.linalg.solve(A,B)
for i in range(len(x)):
    print(varlist[i],float(x[i]) )
