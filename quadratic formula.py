from math import *
negative_sq = False
def quadratic(a, b, c):
    negative_sq = False
    if b<0 and a>0 and c>0:
        negative_sq = True
        b = -1*b
    product = a*c
    addition = b
    factorslist = {}
    coefficient = []
    if product<0:
        for i in range (product,-1):
            if ceil(product/i) == (product/i):
                factorslist[i] = product/i
        print(factorslist)
    if product>0:
        for i in range (1,product+1):
            if ceil(product/i) == (product/i):
                factorslist[i] = product/i
        print(factorslist)
    for i in factorslist.keys():
        if i+factorslist[i] == addition and negative_sq == False:
            coeff1 = c/(-1*i)
            coeff2 = (-1*i)/a
            print(i)
            print(factorslist[i])
            coefficient.append(coeff1)
            if coeff2 != coeff1:
                coefficient.append(coeff2)

        elif i+factorslist[i] == addition and negative_sq == True:
            coeff1 = c/i
            coeff2 = i/a
            coefficient.append(coeff1)
            if coeff2 != coeff1:
                coefficient.append(coeff2)

    print("x =",coefficient)
while True:
    a = int(input("A:"))
    b = int(input("B:"))
    c = int(input("C:"))
    quadratic(a,b,c)
    negative_sq = False
        
    
        
