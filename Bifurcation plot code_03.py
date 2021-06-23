import turtle
def findx(rate,x):
    return rate*x*(1-x)
start = 2
end = 4
n = 100
g = 100
startx = 0.64
cs = (end-start)/100
lx = []
lc = []
for c in range(start*100,end*100,int(cs*100)):
    x = startx
    for i in range(g):
        x = findx(c/100,x)
        p = 0
        while p<n:
            x = findx(c/100,x)
            lc.append(c/100)
            lx.append(x)
            p = p+1
pen = turtle.Pen()
pen.ht()
print(lc)
pen.speed(10)
for i in range(len(lc)):
    pen.penup()
    print("done")
    pen.goto(lc[i],lx[i])
    pen.pendown()
    pen.circle(1)
    

