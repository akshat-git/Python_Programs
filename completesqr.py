from math import *

def complete_the_square(a_begin, b_begin, c_begin):

    for i in range(1, abs(a_begin)+1):
        if a_begin%i == 0 and b_begin%i == 0 and c_begin%i == 0:
            a = a_begin/i
            b = b_begin/i
            c = c_begin/i
    
    a2 = a
    ab = b
    real_c = ((ab/2)/sqrt(a2))**2

    x = int(a2**.5)
    y = real_c **.5

    c_other = -1*c
    c_other += real_c
    sqrt_whole = False
    if sqrt(c_other) % 1 == 0:
        sqrt_whole = True    
    if sqrt_whole:
        case1 = "x = "+str((sqrt(c_other)-y)/x)
        case2 = "x = "+str((-1*(sqrt(c_other))-y)/x)
    if not sqrt_whole:
        case1 = str(x)+"x + "+str(y) +" = -/"+str(c_other)
        case2 = str(x)+"x + "+str(y) +" = - -/"+str(c_other)
    print(case1)
    print(case2)

while True:
    a_in = int(input("A: "))
    b_in = int(input("B: "))
    c_in = int(input("C: "))
    complete_the_square(a_in, b_in, c_in)

