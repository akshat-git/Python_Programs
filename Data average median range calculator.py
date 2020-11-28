
'''
This code takes the numbers entered and finds the mean, median, range,
smallest number, and biggest number
'''
import math
numlist=[]
maxnum = 0
minnum = 0
median = 0
done = False
print("This program takes a list and deterines the mean, median, and range")
print("Type 'quit' to exit and calculate the answers")
while done == False:
    newnum = input("What number do you want to enter? ")
    if newnum == "quit":
        numave = sum(numlist)/(len(numlist))
        done = True
    else: 
        newnum=int(newnum)
        numlist.append(newnum)
numlist.sort()
num=(len(numlist)+1)/2
if math.ceil(num) == math.floor(num):
    median = numlist[math.ceil(num)-1]
else:
    median = (numlist[math.ceil(num)-1] + numlist[math.floor(num)-1])/2

print("Mean:",numave)
print("Median:", median)
print("Range:",max(numlist)-min(numlist))
print("Biggest number:",max(numlist))
print("Smallest number:",min(numlist))
