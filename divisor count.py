from math import *
while True:
    n = int(input("input: "))
    for i in range(n):
        y = []
        z = []
        x = [i for i in range(1,n+1) if not n % i]
        for i in x:
            if i%2 == 0:
                y.append(i)
        for i in x:
            if sqrt(i)%1 ==0:
                z.append(i)
    print("Divisors:",len(x))
    print("Sum:",sum(x))
    print()
    print("Evens:",len(y))
    print("Odds:",len(x)-len(y))
    print("Squares:",len(z))
        
    
