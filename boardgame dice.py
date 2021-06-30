import random
innum = int(input("number:"))
detail = int(input("detail:"))
avgset = []
def rolls(rollnum):
    i = 0
    num = 0
    while i < rollnum:
        i = i+random.randint(0,6)
        num = num + 1
    return num
    
    
for i in range(detail):
    x = rolls(innum)
    avgset.append(x)
    
sumnum = 0
avg = 0
for i in avgset:
    sumnum = sumnum+i
avg = sumnum/detail
print(avg)
