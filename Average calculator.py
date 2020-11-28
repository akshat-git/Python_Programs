# calculates average and biggest number out of all the numbers given
numset = [0]
done = False
maxnum = 0
while done == False:
    newnum = input("What number do you want to enter? ")
    if newnum == "quit":
        print("BYE !!")
        numsum = sum(numset)/(len(numset)-1)
        print("This is the average of your numbers:",numsum)
        print("And this is the biggest number you entered:",maxnum)
        done = True
    elif int(newnum) >= maxnum:
        maxnum = int(newnum)
    else:
        newnum=int(newnum)
        numset.append(newnum)
