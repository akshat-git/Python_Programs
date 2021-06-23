x = int(input("Num: "))
y = int(input("Num: "))
beg = int(input("Start: "))
end = int(input("End: "))
def gcd(x,y):
    gcd = 0
    for i in range(1,max(x,y)):
        if x % i == 0 and y % i == 0:
            gcd = i
    return i
def lcm(gcd,x,y):
    lcm = int(x*y/gcd)
    return lcm
lcm = lcm(gcd(x,y),x,y)
n = 0
for i in range(beg, end+1):
    if i % lcm == 0:
        n += 1
print(n)
    


    
