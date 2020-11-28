from math import *
a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:")) 
x = (sqrt((b**2)-(4*a*c))/(4*(a**2)))-b
print("+-",x,"/",2*a)
