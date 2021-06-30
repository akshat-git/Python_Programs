"""
For the input area write your input as #stones,s,#sticks,order ex: 10s3, or 7s4o
For the min each, type the minimum number of objects in each container
"""
def fact(x):
    numsum = 1
    for i in range(1,x+1):
        numsum = numsum*i
    return numsum


def choose(n,k):
    z = int(((fact(n)/fact(n-k))/fact(k)))
    return z


def stickstone(inp,each,order):
    orderamount = 1
    inp = inp.split("s")
    for i in range(len(inp)):
        inp[i] = int(inp[i])
    each = int(each)
    k = inp[1]
    n = inp[0]
    if order == True:
        orderamount = fact(n)
    
    return choose((n-(each*k))+k-1,k-1)*orderamount


while True:
    order = False
    inp = input("input: ")
    end = len(inp)
    each = input("min each: ")
    if inp[end-1] == "o":
        inp = inp.replace("o","")
        order = True
        
        
    print(stickstone(inp,each,order))

    
