from random import *
from math import *
mean = int(input("What is the mean: "))
sigma =  int(input("What is sigma: "))
detail = int(input("Number of trials"))
numset = []
for i in range(1*detail):
    x = mean-(sigma*5)
    y = mean-(sigma*4)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(2*detail):
    x = mean-(sigma*4)
    y = mean-(sigma*3)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(4*detail):
    x = mean-(sigma*3)
    y = mean-(sigma*2)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(8*detail):
    x = mean-(sigma*2)
    y = mean-(sigma*1)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(12*detail):
    x = mean-(sigma*1)
    y = mean-(sigma*0)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(39*detail):
    x = mean+(sigma*0.3)
    y = mean-(sigma*0.3)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(12*detail):
    x = mean+(sigma*0)
    y = mean+(sigma*1)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(8*detail):
    x = mean+(sigma*1)
    y = mean+(sigma*2)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(4*detail):
    x = mean+(sigma*2)
    y = mean+(sigma*3)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(2*detail):
    x = mean+(sigma*3)
    y = mean+(sigma*4)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
for i in range(1*detail):
    x = mean+(sigma*4)
    y = mean+(sigma*5)
    num = uniform(x,y)
    num = round(num,2)
    numset.append(num)
print(numset)
