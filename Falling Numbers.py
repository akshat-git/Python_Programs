numsum = 0
def fact(x):
    numsum = 1
    for i in range(1,x+1):
        numsum = numsum*i
    return numsum
def choose(n,k):
    z = int(((fact(n)/fact(n-k))/fact(k)))
    return z
while True:
    dig = int(input("Digit #: "))
    print(choose(10,dig)   
