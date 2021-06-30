cox = int(input("Coefficient of x: "))
coy = int(input("Coefficient of y: "))*-1
numsum = int(input("Integer: "))
total = (cox-numsum)/coy
print("(",cox,"x ",-1*numsum,")/",coy," = y",sep = "")
