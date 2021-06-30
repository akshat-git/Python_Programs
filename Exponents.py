while True:
    ans = 1
    x = float(input("Base: "))
    y = int(input("Exponent:"))
    negative = False
    if y<0:
        y = abs(y)
        negative = True
    if negative == True:
        ans = "1 / "+str(ans*(x**y))
    else:
        ans = str(ans*(x**y))
    print(ans)
