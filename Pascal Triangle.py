numlist = []
cycles = int(input("Cycle number: "))
newlist = []
strlist = ""

print("1")
for i in range(cycles):
    for j in range(len(numlist)-1):
        newlist.append((numlist[j])+numlist[j+1])
    numlist = [1]
    for k in newlist:
        numlist.append(k)
    numlist.append(1)
    for l in numlist:
        strlist = strlist+str(l)+" "
    print(strlist)
    strlist = ""
    newlist = []
    
