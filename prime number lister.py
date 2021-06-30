from math import *
num = 3
print("2")
while True:
    prime = True
    for i in range(floor(num**(1/2))):
        if num%(i+2) == 0:
            prime = False
    if prime == True:
        print(num)
    num = num+2

