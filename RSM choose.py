def factorial(x):
    numsum = 1
    for i in range(1,x+1):
        numsum = numsum*i
    return numsum
def choose(x,y):
    n = int(x)
    k = int(y)
    z = int(((factorial(n)/factorial(n-k))/factorial(k)))
    print(z)
while True:
    choosein = input("input: ").split("c")
    choose(choosein[0],choosein[1])
    
    

