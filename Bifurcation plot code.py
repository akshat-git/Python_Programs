import matplotlib.pylab as plt
def findx(rate,x):
    return rate*x*(1-x)
start = 2
end = 4
n = 100
g = 100
startx = 0.64
cs = (end-start)/1000
lx = []
lc = []
for c in range(start*1000,end*1000,int(cs*1000)):
    x = startx
    for i in range(g):
        x = findx(c/1000,x)
        p = 0
        while p<n:
            x = findx(c/1000,x)
            lc.append(c/1000)
            lx.append(x)
            p = p+1
plt.xlabel("Rate")
plt.ylabel("Populations")
plt.plot(lc,lx,'.',linewidth = 0.01)
plt.show()

