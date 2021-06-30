def factorial(x):
    numsum = 1
    for i in range(1,x+1):
        numsum = numsum*i
    return numsum
while True:
    y = int(input("factorial: "))
    rep = int(input("reps: "))+1
    print(factorial(y)/rep)
