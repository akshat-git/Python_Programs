unit = input("what is the unit? ")
pyrasize = int(input("How big do you want your pyramid to be? "))
for i in range (pyrasize):
    layer = i*(unit+" ")
    print(" "*(pyrasize-i),layer)
