x = int(input("Num: "))
y = int(input("Num: "))

start = 0

while x >= 1 and y >= 1:
    if x>y:
        x = x-y
        start+=1
    if y>x:
        y = y-x
        start+=1
    if y == x:
        y = 0
        x = 0
        start+=1
print(start)
        
