
numgoto = int(input("How many members of the sequence do you want? "))
numlist = [0,1]
print(0)
print(1)
for i in range(numgoto):
    numlist.append(numlist[i+1]+numlist[i])
    print(numlist[i+2])

