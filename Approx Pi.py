def getpi(iternum):
    pi = 0
    for i in range(iternum):
        if i % 2 == 0:
            pi = pi+(1/(2*i+1))
        else:
            pi = pi-(1/(2*i+1))
    return pi * 4
itertotal = int(input("Iteration count: "))
print(getpi(itertotal))
